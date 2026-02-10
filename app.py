import streamlit as st
import time

# --- Login logic (as before) ---
USERNAME = "denian"
PASSWORD = "onlyyou"
MAX_ATTEMPTS = 3

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "locked" not in st.session_state:
    st.session_state.locked = False

if st.session_state.locked:
    st.error("Too many attempts. This page is temporarily locked.")
else:
    if not st.session_state.logged_in:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.success("Login successful!")
            else:
                st.session_state.attempts += 1
                st.error("Incorrect username or password.")
                if st.session_state.attempts >= MAX_ATTEMPTS:
                    st.session_state.locked = True
    else:
        st.title("Welcome to Heartbreak Slides 💔")
        # Instead of time.sleep, use a placeholder for effect
        placeholder = st.empty()
        for i in range(1, 6):
            placeholder.text(f"Loading slides... {i*20}%")
            time.sleep(0.3)  # this is okay for small delays
        placeholder.empty()
        st.write("Here’s your full content! Add your slides below.")
