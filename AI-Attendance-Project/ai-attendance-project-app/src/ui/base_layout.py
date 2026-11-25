import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #101820 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background: linear-gradient(145deg, #fff0ed 0%, #f5c4bc 100%) !important;
                    padding:2rem !important;
                    border: 1px solid #df6b5d !important;
                    border-radius: 1.25rem !important;
                    min-height: 18rem !important;
                    box-shadow: 0 1.25rem 2.5rem rgba(0, 0, 0, 0.16) !important;
                    transition: transform 180ms ease, box-shadow 180ms ease !important;
                    }

                .stApp div[data-testid="stColumn"]:hover {
                    transform: translateY(-4px) !important;
                    box-shadow: 0 1.5rem 3rem rgba(0, 0, 0, 0.24) !important;
                }

                .stApp div[data-testid="stColumn"]:first-child:hover {
                    background: linear-gradient(145deg, #d9f2e7 0%, #b9e5d1 100%) !important;
                    border-color: #39a96b !important;
                    box-shadow: 0 1.5rem 3rem rgba(35, 145, 91, 0.28) !important;
                }

                .stApp div[data-testid="stColumn"]:last-child:hover {
                    background: linear-gradient(145deg, #d9f2e7 0%, #b9e5d1 100%) !important;
                    border-color: #39a96b !important;
                    box-shadow: 0 1.5rem 3rem rgba(35, 145, 91, 0.28) !important;
                }

                .stApp div[data-testid="stColumn"] button {
                    background: #c44b3e !important;
                    border-color: #c44b3e !important;
                    color: #ffffff !important;
                    transition: background-color 180ms ease, border-color 180ms ease, transform 180ms ease !important;
                }

                .stApp div[data-testid="stColumn"] button:hover {
                    background: #23915b !important;
                    border-color: #23915b !important;
                    transform: translateY(-2px) !important;
                }

                @media (max-width: 640px) {
                    .block-container {
                        padding-left: 1rem !important;
                        padding-right: 1rem !important;
                    }

                    .stApp div[data-testid="stColumn"] {
                        min-height: 14rem !important;
                        padding: 1.35rem !important;
                    }
                }

                .stApp div[data-testid="stColumn"] h2,
                .stApp div[data-testid="stColumn"] h3 {
                    color: #101820 !important;
                }

                .stApp div[data-testid="stColumn"] p {
                    color: #40505a !important;
                }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #f2eee7 !important;
                }

                .stApp [data-testid="stHeader"] {
                    background: transparent !important;
                }

                .stApp [data-testid="stTextInput"] input,
                .stApp [data-testid="stNumberInput"] input,
                .stApp [data-testid="stTextArea"] textarea {
                    background: #fffdf9 !important;
                    border: 1px solid #c8d1ce !important;
                    border-radius: 0.75rem !important;
                    color: #101820 !important;
                    padding: 0.8rem 1rem !important;
                }

                .stApp [data-testid="stTextInput"] input:focus,
                .stApp [data-testid="stNumberInput"] input:focus,
                .stApp [data-testid="stTextArea"] textarea:focus {
                    border-color: #0d8b83 !important;
                    box-shadow: 0 0 0 2px rgba(13, 139, 131, 0.14) !important;
                }

                .stApp [data-testid="stCameraInput"],
                .stApp [data-testid="stFileUploader"] {
                    background: #fffdf9 !important;
                    border: 1px dashed #9aaba8 !important;
                    border-radius: 1rem !important;
                    padding: 0.75rem !important;
                }

                .stApp label,
                .stApp .stMarkdown p {
                    color: #40505a;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #0d8b83 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="primary"],
            div.stButton > button[kind="primary"] {
                background-color: #0d8b83 !important;
                border-color: #0d8b83 !important;
                color: #ffffff !important;
            }

            button[kind="primary"]:hover,
            div.stButton > button[kind="primary"]:hover {
                background-color: #08766f !important;
                border-color: #08766f !important;
            }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #c44b3e !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]:hover {
                background-color: #a83b32 !important;
            }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #dbe9e5 !important;
                color: #101820 !important;
                padding: 10px 20px !important;
                border: 1px solid #b8cbc7 !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]:hover {
                background-color: #c8ded9 !important;
                border-color: #0d8b83 !important;
            }

            .stApp [data-testid="stMetric"] {
                background: #fffdf9 !important;
                border: 1px solid #c8d1ce !important;
                border-radius: 0.85rem !important;
                padding: 0.8rem 1rem !important;
            }

            .stApp [data-testid="stDataFrame"] {
                border: 1px solid #c8d1ce !important;
                border-radius: 0.85rem !important;
                overflow: hidden !important;
            }

            button:hover{
                transform :scale(1.05);
                filter: brightness(0.9);
                }
        </style>  

                """
            ,unsafe_allow_html=True)