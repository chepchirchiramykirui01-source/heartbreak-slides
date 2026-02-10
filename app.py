import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(page_title="For Denian", layout="centered")

# ---------------- Dark Theme ----------------
st.markdown(
    """
    <style>
    body { background-color: #0b0b0f; color: #e5e5e5; font-family: 'Helvetica', sans-serif;}
    .stApp { background: linear-gradient(180deg, #0b0b0f, #12121a); padding: 20px; }
    h1, h2, h3 { color: #f2f2f2; }
    .stButton>button { background-color: #ff4b5c; color: white; border-radius: 10px; padding: 10px 20px;}
    .stTextArea>div>textarea { background-color: #1c1c27; color: #e5e5e5; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- Login Config ----------------
USERNAME = "denian"
PASSWORD = "onlyyou"
MAX_ATTEMPTS = 3

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "attempts" not in st.session
