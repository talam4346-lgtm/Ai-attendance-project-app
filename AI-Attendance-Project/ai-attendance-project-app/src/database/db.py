from src.database.config import get_supabase
import bcrypt
import json
from datetime import datetime
from pathlib import Path

LOCAL_DB_PATH = Path(__file__).resolve().parent / "local_data.json"


def _database():
    return get_supabase()


def _local_data():
    if not LOCAL_DB_PATH.exists():
        return {"teachers": [], "students": [], "subjects": [], "enrollments": [], "attendance": []}
    return json.loads(LOCAL_DB_PATH.read_text(encoding="utf-8"))


def _save_local_data(data):
    LOCAL_DB_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _next_id(items, key):
    return max((item.get(key, 0) for item in items), default=0) + 1


def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()


def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


def check_teacher_exists(username):
    database = _database()
    if database:
        response = database.table("teachers").select("username").eq("username", username).execute()
        return len(response.data) > 0
    return any(teacher["username"] == username for teacher in _local_data()["teachers"])


def create_teacher(username, password, name):
    database = _database()
    data = {"username": username, "password": hash_pass(password), "name": name}
    if database:
        return database.table("teachers").insert(data).execute().data
    local = _local_data()
    data["teacher_id"] = _next_id(local["teachers"], "teacher_id")
    local["teachers"].append(data)
    _save_local_data(local)
    return [data]


def teacher_login(username, password):
    database = _database()
    if database:
        response = database.table("teachers").select("*").eq("username", username).execute()
        teachers = response.data
    else:
        teachers = [teacher for teacher in _local_data()["teachers"] if teacher["username"] == username]
    if teachers and check_pass(password, teachers[0]["password"]):
        return teachers[0]
    return None


def get_all_students():
    database = _database()
    if database:
        return database.table("students").select("*").execute().data
    return _local_data()["students"]


def create_student(new_name, face_embedding=None, voice_embedding=None):
    database = _database()
    data = {"name": new_name, "face_embedding": face_embedding, "voice_embedding": voice_embedding}
    if database:
        return database.table("students").insert(data).execute().data
    local = _local_data()
    data["student_id"] = _next_id(local["students"], "student_id")
    local["students"].append(data)
    _save_local_data(local)
    return [data]


def create_subject(subject_code, name, section, teacher_id):
    database = _database()
    data = {"subject_code": subject_code, "name": name, "section": section, "teacher_id": teacher_id}
    if database:
        return database.table("subjects").insert(data).execute().data
    local = _local_data()
    data["subject_id"] = _next_id(local["subjects"], "subject_id")
    local["subjects"].append(data)
    _save_local_data(local)
    return [data]


def get_teacher_subjects(teacher_id):
    database = _database()
    if database:
        subjects = database.table("subjects").select("*, subject_students(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id).execute().data
        for subject in subjects:
            subject["total_students"] = subject.get("subject_students", [{}])[0].get("count", 0)
            subject["total_classes"] = len({log["timestamp"] for log in subject.get("attendance_logs", [])})
            subject.pop("subject_students", None)
            subject.pop("attendance_logs", None)
        return subjects
    local = _local_data()
    subjects = [subject.copy() for subject in local["subjects"] if subject["teacher_id"] == teacher_id]
    for subject in subjects:
        subject["total_students"] = sum(item["subject_id"] == subject["subject_id"] for item in local["enrollments"])
        subject["total_classes"] = len({item.get("timestamp") for item in local["attendance"] if item.get("subject_id") == subject["subject_id"]})
    return subjects


def get_subject_students(subject_id):
    database = _database()
    if database:
        return database.table("subject_students").select("*, students(*)").eq("subject_id", subject_id).execute().data
    local = _local_data()
    students = {student["student_id"]: student for student in local["students"]}
    return [{**item, "students": students.get(item["student_id"])} for item in local["enrollments"] if item["subject_id"] == subject_id]


def get_subject_by_code(subject_code):
    database = _database()
    if database:
        response = database.table("subjects").select("subject_id, name, subject_code").eq("subject_code", subject_code).execute()
        return response.data[0] if response.data else None
    return next((subject for subject in _local_data()["subjects"] if subject["subject_code"] == subject_code), None)


def is_student_enrolled(student_id, subject_id):
    database = _database()
    if database:
        response = database.table("subject_students").select("*").eq("subject_id", subject_id).eq("student_id", student_id).execute()
        return bool(response.data)
    return any(item["subject_id"] == subject_id and item["student_id"] == student_id for item in _local_data()["enrollments"])


def enroll_student_to_subject(student_id, subject_id):
    database = _database()
    data = {"student_id": student_id, "subject_id": subject_id}
    if database:
        return database.table("subject_students").insert(data).execute().data
    local = _local_data()
    if not any(item == data for item in local["enrollments"]):
        local["enrollments"].append(data)
        _save_local_data(local)
    return [data]


def unenroll_student_to_subject(student_id, subject_id):
    database = _database()
    if database:
        return database.table("subject_students").delete().eq("student_id", student_id).eq("subject_id", subject_id).execute().data
    local = _local_data()
    local["enrollments"] = [item for item in local["enrollments"] if not (item["student_id"] == student_id and item["subject_id"] == subject_id)]
    _save_local_data(local)
    return []


def get_student_subjects(student_id):
    database = _database()
    if database:
        return database.table("subject_students").select("*, subjects(*)").eq("student_id", student_id).execute().data
    local = _local_data()
    subjects = {subject["subject_id"]: subject for subject in local["subjects"]}
    return [{**item, "subjects": subjects.get(item["subject_id"])} for item in local["enrollments"] if item["student_id"] == student_id]


def get_student_attendance(student_id):
    database = _database()
    if database:
        return database.table("attendance_logs").select("*, subjects(*)").eq("student_id", student_id).execute().data
    local = _local_data()
    subjects = {subject["subject_id"]: subject for subject in local["subjects"]}
    return [{**item, "subjects": subjects.get(item.get("subject_id"))} for item in local["attendance"] if item.get("student_id") == student_id]


def create_attendance(logs):
    database = _database()
    if database:
        return database.table("attendance_logs").insert(logs).execute().data
    local = _local_data()
    entries = logs if isinstance(logs, list) else [logs]
    for entry in entries:
        entry = dict(entry)
        entry.setdefault("timestamp", datetime.now().isoformat())
        local["attendance"].append(entry)
    _save_local_data(local)
    return entries


def get_attendance_for_teacher(teacher_id):
    database = _database()
    if database:
        return database.table("attendance_logs").select("*, subjects!inner(*)").eq("subjects.teacher_id", teacher_id).execute().data
    local = _local_data()
    subject_ids = {subject["subject_id"] for subject in local["subjects"] if subject["teacher_id"] == teacher_id}
    subjects = {subject["subject_id"]: subject for subject in local["subjects"]}
    return [
        {**item, "subjects": subjects.get(item.get("subject_id"))}
        for item in local["attendance"]
        if item.get("subject_id") in subject_ids
    ]

