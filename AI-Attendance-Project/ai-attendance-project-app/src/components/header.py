import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin:1.5rem 0 2.75rem; text-align:center">
            <div style="color:#d8a25e; font-family:'Outfit', sans-serif; font-size:0.72rem; font-weight:700; letter-spacing:0.22rem; margin-bottom:0.85rem">AI ATTENDANCE / SMART CLASSROOM</div>
            <img src='{logo_url}' alt='SnapClass logo' style='height:88px; width:88px; object-fit:contain; margin-bottom:0.7rem;' />
            <h1 style='color:#f5f0e8; font-size:clamp(2.8rem, 7vw, 5.6rem) !important; letter-spacing:0.08rem; line-height:0.88 !important;'>SNAP<br/>CLASS</h1>
            <p style="color:#b9c5c7; font-family:'Outfit', sans-serif; font-size:1.05rem; margin-top:1rem; max-width:30rem">Attendance that feels effortless, accurate, and ready for every classroom.</p>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:0.7rem; padding:0.35rem 0 1.1rem">
            <img src='{logo_url}' alt='SnapClass logo' style='height:58px; width:58px; object-fit:contain;' />
            <div>
                <div style="color:#0d8b83; font-family:'Outfit', sans-serif; font-size:0.62rem; font-weight:700; letter-spacing:0.16rem">AI ATTENDANCE</div>
                <h2 style='text-align:left; color:#101820; font-size:1.45rem !important; letter-spacing:0.04rem; line-height:0.86 !important; margin:0 !important'>SNAP<br/>CLASS</h2>
            </div>
        </div>   
                
                """, unsafe_allow_html=True)
