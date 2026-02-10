{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fswiss\fcharset0 Helvetica-Bold;\f2\fnil\fcharset0 AppleColorEmoji;
\f3\fnil\fcharset128 HiraginoSans-W3;\f4\fnil\fcharset77 ZapfDingbatsITC;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Heartbreak Slides App \'96 Dark Aesthetic + Full Login Logic (Python)\
# Run with: streamlit run app.py\
\
import streamlit as st\
import time\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\tx16365\pardirnatural\partightenfactor0
\cf0 st.set_page_config(page_title="For Denian", layout="centered")\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \
# ---------------- DARK THEME ----------------\
st.markdown(\
    """\
    <style>\
    body \{ background-color: #0b0b0f; color: #e5e5e5; \}\
    .stApp \{ background: linear-gradient(180deg, #0b0b0f, #12121a); \}\
    h1, h2, h3 \{ color: #f2f2f2; \}\
    </style>\
    """,\
    unsafe_allow_html=True,\
)\
\
# ---------------- LOGIN CONFIG ----------------\
USERNAME = "denian"\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 PASSWORD = "onlyyou"
\f1\b \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\b0 \cf0 MAX_ATTEMPTS = 3\
\
if "logged_in" not in st.session_state:\
    st.session_state.logged_in = False\
\
if "attempts" not in st.session_state:\
    st.session_state.attempts = 0\
\
if "locked" not in st.session_state:\
    st.session_state.locked = False\
\
# ---------------- LOCKOUT LOGIC ----------------\
if st.session_state.locked:\
    st.error("Too many attempts. This page is closed.")\
    st.stop()\
\
# ---------------- LOGIN PAGE ----------------\
if not st.session_state.logged_in:\
    st.markdown("## 
\f2 \uc0\u55357 \u56594 
\f0  Private Page")\
    st.write("Some words are not meant for everyone.")\
\
    username = st.text_input("Username")\
    password = st.text_input("Password", type="password")\
\
    if st.button("Enter"):\
        if username == USERNAME and password == PASSWORD:\
            st.session_state.logged_in = True\
            st.session_state.attempts = 0\
            st.rerun()\
        else:\
            st.session_state.attempts += 1\
            remaining = MAX_ATTEMPTS - st.session_state.attempts\
            if remaining <= 0:\
                st.session_state.locked = True\
                st.error("Access permanently denied.")\
            else:\
                st.error(f"Wrong details. \{remaining\} attempt(s) left.")\
\
    st.stop()\
\
# ---------------- SLIDES ----------------\
slides = [\
    ("Denian", "This isn\'92t blame. This is truth, written in the dark."),\
    ("I Loved You", "I loved you fiercely, with fear of losing you."),\
    ("I Was Overprotective", "I held on too tight, thinking love meant guarding."),\
    ("My Fear", "My fear slowly became the thing that pushed you away."),\
    ("I See It Now", "I confused control with care."),\
    ("The Distance", "You pulled away quietly, and I felt it."),\
    ("What I Regret", "I regret not trusting you enough."),\
    ("What Hurts", "It hurts knowing my love became heavy."),\
    ("I Own It", "This isn\'92t victimhood. I take responsibility."),\
    ("Still", "I don\'92t regret loving you. Only how fear shaped it."),\
    ("Letting Go", "Loving you also means releasing you."),\
    ("Goodbye", "This is where it ends. Quietly.")\
]\
\
# ---------------- NAVIGATION ----------------\
if "index" not in st.session_state:\
    st.session_state.index = 0\
\
st.markdown(f"## \{slides[st.session_state.index][0]\}")\
st.write(slides[st.session_state.index][1])\
\
col1, col2, col3 = st.columns(3)\
\
with col1:\
    if st.button("
\f3 \uc0\u11013 
\f0  Previous"):\
        st.session_state.index = max(0, st.session_state.index - 1)\
\
with col3:\
    if st.button("Next 
\f4 \uc0\u10145 
\f0 "):\
        st.session_state.index += 1\
\
# ---------------- AUTO LOGOUT ON FINAL SLIDE ----------------\
if st.session_state.index >= len(slides):\
    st.markdown("### Session ended")\
    st.write("You\'92ve reached the end. This page will close.")\
    time.sleep(3)\
    st.session_state.logged_in = False\
    st.session_state.index = 0\
    st.rerun()\
\
st.progress((st.session_state.index + 1) / len(slides))\
\
st.markdown("---")\
if st.button("Log out now"):\
    st.session_state.logged_in = False\
    st.session_state.index = 0\
    st.rerun()\
}
