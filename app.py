# Heartbreak Slides App – Dark Aesthetic + Full Login Logic (Python)
# Run with: streamlit run app.py

import streamlit as st
import time

st.set_page_config(page_title="For Denian", layout="centered")

# ---------------- DARK THEME ----------------
st.markdown(
    """
    <style>
    body { background-color: #0b0b0f; color: #e5e5e5; }
    .stApp { background: linear-gradient(180deg, #0b0b0f, #12121a); }
    h1, h2, h3 { color: #f2f2f2; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- LOGIN CONFIG ----------------
USERNAME = "denian"
PASSWORD = "onlyyou"
MAX_ATTEMPTS = 3

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "locked" not in st.session_state:
    st.session_state.locked = False

# ---------------- LOCKOUT LOGIC ----------------
if st.session_state.locked:
    st.error("Too many attempts. This pag

