import streamlit as st

# Page config
st.set_page_config(page_title="For Denian", layout="centered")

# Dark theme
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

# Login config
USERNAME = "denian"
PASSWORD = "onlyyou"
MAX_ATTEMPTS = 3

# Session state defaults
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "locked" not in st.session_state:
    st.session_state.locked = False

# Lockout check
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
                st.success("Welcome!")
            else:
                st.session_state.attempts += 1
                st.error("Incorrect username or password.")
                if st.session_state.attempts >= MAX_ATTEMPTS:
                    st.session_state.locked = True
    else:
        st.title("Welcome to Heartbreak Slides 💔")
        st.write("You are logged in. Here's your content.")
        # Add the rest of your app content here
