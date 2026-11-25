import os

import streamlit as st
from supabase import Client, create_client


def _read_setting(name):
    try:
        value = st.secrets.get(name)
    except Exception:
        value = None
    return value or os.getenv(name)


def get_supabase() -> Client | None:
    url = _read_setting("SUPABASE_URL")
    key = _read_setting("SUPABASE_KEY")
    if not url or not key:
        return None
    return create_client(url, key)


supabase: Client | None = None
try:
    supabase = get_supabase()
except RuntimeError:
    pass