import base64
from pathlib import Path

import streamlit as st


LOGO_PATH = Path(__file__).resolve().parents[1] / "assets" / "tanveer_alam.png"


def _logo_data_uri():
    encoded_logo = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded_logo}"


def _render_footer(text_color):
    logo_url = _logo_data_uri()

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:{text_color};"> Created with ❤️ by Tanveer Alam </p>
        <img src='{logo_url}' alt='Tanveer Alam' style='height:25px; width:25px; border-radius:50%;' />
        </div>
        """, unsafe_allow_html=True)


def footer_home():
    _render_footer("white")


def footer_dashboard():
    _render_footer("black")
