import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(page_title="For Denian", layout="centered")

# ---------------- Dark & Heartbreak Theme ----------------
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
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "locked" not in st.session_state:
    st.session_state.locked = False
if "current_slide" not in st.session_state:
    st.session_state.current_slide = 0
if "comments" not in st.session_state:
    st.session_state.comments = [""] * 15  # empty comments for each slide

# ---------------- Heartbreak Slides ----------------
slides = [
"""💔 Slide 1: Memories of You
I still remember the first time our paths crossed, the way your laughter echoed in my mind long after you left...
""",
"""💔 Slide 2: Lonely Streets
Walking alone, streets empty, I hear echoes of our conversations in the wind...
""",
"""💔 Slide 3: Letters I Never Sent
I wrote words I never had the courage to say, pouring my soul into letters I never sent...
""",
"""💔 Slide 4: Shadows of Your Voice
Even now, I hear your voice in the rustling leaves, the hum of a distant train...
""",
"""💔 Slide 5: The Anime Sky
I remember us staring at sunsets that looked like anime skies, painted in shades of fire and gold...
""",
"""💔 Slide 6: Quiet Nights
Nights are hardest. The city sleeps, but my mind races...
""",
"""💔 Slide 7: Rain and Remembrance
Rain taps against my window, a rhythm that echoes my heartbeats...
""",
"""💔 Slide 8: Music and Pain
Every song I hear seems to carry your voice, the echo of moments we shared...
""",
"""💔 Slide 9: Letters to the Wind
I speak to the wind now, sending letters that drift where you might never read them...
""",
"""💔 Slide 10: Fragments of Us
I collect fragments of us in my mind—the jokes, the fights, the late-night talks...
""",
"""💔 Slide 11: Silence Speaks
Sometimes, silence speaks louder than words. I hear it in the empty apartment...
""",
"""💔 Slide 12: Longing and Hope
Even in longing, there is hope. I imagine anime skies where light breaks through dark clouds...
""",
"""💔 Slide 13: Walking Forward
I walk forward now, even with pieces of you still inside me...
""",
"""💔 Slide 14: Stars and Reflection
Under the stars, I reflect on all we were...
""",
"""💔 Slide 15: A New Dawn
The sun rises on a world that feels different, yet familiar...
"""
]

# ---------------- Login / Logout ----------------
def show_login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.session_state.attempts = 0
            st.success("Login successful! 💖")
        else:
            st.session_state.attempts += 1
            st.error("Incorrect username or password ❌")
            if st.session_state.attempts >= MAX_ATTEMPTS:
                st.session_state.locked = True

def show_logout():
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_slide = 0
        st.success("Logged out successfully 💔")

# ---------------- Main App ----------------
if st.ses
