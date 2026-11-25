# AI Attendance Project

## Start the app

Double-click `run_app.bat`, then open:

http://localhost:8501

Or run from PowerShell:

```powershell
cd "C:\Users\Altmas quraishi\Desktop\AI-Attendance-Project\ai-attendance-project-app"
python -m streamlit run app.py
```

## First use

1. Choose **Teacher**.
2. Register or log in with the saved teacher account.
3. Create a subject.
4. Enroll students and register their face data.
5. Use **Take Attendance** to scan photos.

The app has a local database fallback, so it works without Supabase credentials. Local users, subjects, students, and attendance are saved in `src/database/local_data.json`. This file is intentionally ignored by Git because it contains local account and attendance data.

If Supabase is configured later, create `.streamlit/secrets.toml` with:

```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
```

The existing branding and demo assets are already saved in this project.