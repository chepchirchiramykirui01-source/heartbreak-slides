import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(page_title="For Denian", layout="wide")

# ---------------- Dark Theme with Background Images ----------------
st.markdown(
    """
    <style>
    body {
        background-color: #0b0b0f;
        color: #e5e5e5;
        font-family: 'Helvetica', sans-serif;
    }
    .stApp {
        padding: 0px 50px 50px 50px;
    }
    h1, h2, h3, p {
        color: #f2f2f2;
    }
    .slide-text {
        font-size: 22px;
        line-height: 1.6;
        padding: 40px;
        background-color: rgba(11,11,15,0.6);
        border-radius: 15px;
    }
    .stButton>button {
        background-color: #ff4b5c;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stTextArea>div>textarea {
        background-color: #1c1c27;
        color: #e5e5e5;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- Login Config ----------------
USERNAME = "denian"
PASSWORD = "onlyyou"
MAX_ATTEMPTS = 3

# ---------------- Slides Content ----------------
slides = [
    "💔 Slide 1: Memories of You\nI still remember the first time our paths crossed...",
    "💔 Slide 2: Lonely Streets\nWalking alone, streets empty...",
    "💔 Slide 3: Letters I Never Sent\nI wrote words I never had the courage to say...",
    "💔 Slide 4: Shadows of Your Voice\nEven now, I hear your voice in the rustling leaves...",
    "💔 Slide 5: The Anime Sky\nI remember us staring at sunsets that looked like anime skies...",
    "💔 Slide 6: Quiet Nights\nNights are hardest. The city sleeps, but my mind races...",
    "💔 Slide 7: Rain and Remembrance\nRain taps against my window, a rhythm that echoes my heartbeats...",
    "💔 Slide 8: Music and Pain\nEvery song I hear seems to carry your voice...",
    "💔 Slide 9: Letters to the Wind\nI speak to the wind now, sending letters...",
    "💔 Slide 10: Fragments of Us\nI collect fragments of us in my mind...",
    "💔 Slide 11: Silence Speaks\nSometimes, silence speaks louder than words...",
    "💔 Slide 12: Longing and Hope\nEven in longing, there is hope...",
    "💔 Slide 13: Walking Forward\nI walk forward now, even with pieces of you still inside me...",
    "💔 Slide 14: Stars and Reflection\nUnder the stars, I reflect on all we were...",
    "💔 Slide 15: A New Dawn\nThe sun rises on a world that feels different, yet familiar..."
]

# ---------------- Slide Images ----------------
slide_images = [
    "https://images.unsplash.com/photo-1517256064527-09c73fc73e68?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1528794701846-1a9b80d021d2?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1535413293875-2a4b7b48e468?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1511605969910-891b2f89807f?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1508780709619-79562169bc64?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1526318472351-3c9a36b3c5f7?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1508919801845-fc2ae1bc3f3f?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1508704019884-6b416f3b9f57?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1501869152899-6d50f1d4f6e1?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=1600&q=80"
]

# ---------------- Session State Initialization ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "locked" not in st.session_state:
    st.session_state.locked = False
if "current_slide" not in st.session_state:
    st.session_state.current_slide = 0
if "comments" not in st.session_state:
    st.session_state.comments = [""] * len(slides)

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
if st.session_state.locked:
    st.error("Too many login attempts. You are temporarily locked out.")
elif not st.session_state.logged_in:
    show_login()
else:
    # ---------------- Slide Display ----------------
    slide_idx = st.session_state.current_slide
    st.markdown(
        f"""
        <div style="
            background-image: url('{slide_images[slide_idx]}');
            background-size: cover;
            background-position: center;
            padding: 80px;
            border-radius: 15px;
        ">
            <div class="slide-text">
                {slides[slide_idx].replace('\n', '<br>')}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- Spotify Background Song ----------------
    st.markdown(
        """
        <iframe style="border-radius:12px"
            src="https://open.spotify.com/embed/track/4guQztGKAETkvuTekNeqBe"
            width="300" height="80" frameborder="0"
            allow="encrypted-media; autoplay" allowfullscreen>
        </iframe>
        """,
        unsafe_allow_html=True,
    )

    # ---------------- Slide Navigation ----------------
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        if st.button("⬅ Previous"):
            if st.session_state.current_slide > 0:
                st.session_state.current_slide -= 1

    with col2:
        # Comment Section
        idx = st.session_state.current_slide
        comment = st.text_area(
            "Leave a comment:", 
            value=st.session_state.comments[idx],
            key=f"comment_{idx}"
        )
        if st.button("Submit Comment", key=f"submit_{idx}"):
            st.session_state.comments[idx] = comment
            st.success("Comment saved 💌")

    with col3:
        if st.button("Next ➡"):
            if st.session_state.current_slide < len(slides) - 1:
                st.session_state.current_slide += 1

    # ---------------- Logout ----------------
    show_logout()
