import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:#fffdf9; border-top:4px solid #0d8b83; padding:1.35rem; border-radius:1rem; border:1px solid #c8d1ce; margin-bottom:1rem; box-shadow:0 0.7rem 1.6rem rgba(16,24,32,0.08);">
        <div style="color:#d08d45; font-family:'Outfit', sans-serif; font-size:0.68rem; font-weight:700; letter-spacing:0.14rem; text-transform:uppercase; margin-bottom:0.45rem">Course workspace</div>
        <h3 style="margin:0; color:#101820; font-size:1.4rem ">{name}</h3>
        <p style="color:#5b6b70; margin:0.65rem 0 1rem;">Code: <span style="background:#dbe9e5; color:#08766f; padding:0.25rem 0.55rem; border-radius:0.35rem; font-weight:700;">{code}</span> <span style="margin-left:0.45rem">Section: {section}</span></p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background:#f2eee7; color:#40505a; padding:0.42rem 0.7rem; border-radius:0.55rem; font-size:0.86rem">{icon} <b style="color:#101820">{value}</b> {label}</div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
