import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(page_title="For Denian", layout="wide")

# ---------------- Dark Theme ----------------
st.markdown(
    """
    <style>
    body {background-color: #0b0b0f; color: #ffffff; font-family: 'Helvetica', sans-serif;}
    .stApp {padding: 0px 50px 50px 50px;}
    .slide-text {font-size:22px; line-height:1.6; padding:40px; background-color: rgba(11,11,15,0.7);
                 border-radius:15px; color:#ffffff;}
    .stButton>button {background-color:#ff4b5c; color:white; border-radius:10px; padding:10px 20px; font-size:16px;}
    .stTextArea>div>textarea {background-color:#1c1c27; color:#ffffff; font-size:18px;}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- Login Config ----------------
USERNAME = "denian"
PASSWORD = "onlyyou"
MAX_ATTEMPTS = 3

# ---------------- Slides & Images ----------------
# Each slide 100+ words, casual nonchalant tone
slides = [
    "Slide 1: Waterfall Meeting\nI remember that day perfectly, the waterfall roaring beside us, sunlight on the rocks, and you standing there calm and collected. You didn’t try to impress; yet everything about you felt effortless. You glanced at me briefly, smiled at something small, and I liked that. You were nonchalant, cool, always seemed right, and it was magnetic. We spoke only for a few minutes, shared a laugh, and that was it. Still, the memory lingers. That casual confidence, the quiet correctness, and the cool energy — unforgettable in just one afternoon.",
    
    "Slide 2: Little Details\nYour every move was easy, casual. The way you adjusted your backpack, how you glanced at the water, how you laughed — quiet, understated. You didn’t need to impress, yet I noticed everything. You were right in every small action, always composed, and that made me admire you silently. There’s something about someone being naturally cool and confident without trying, something that sticks in the mind. That day by the waterfall, everything you did felt effortless, like life just aligned when you were around. It was one meeting, yet it felt significant.",
    
    "Slide 3: Watching You\nI remember the brief moments walking along the trail. You were nonchalant, your gaze casual, yet everything about you made sense. Even small actions — tying your shoe, checking your phone — seemed precise. I liked that. You didn’t overthink, didn’t try to be noticed. It was just you being yourself, and it made an impression. I watched you for a few moments, smiled quietly, and felt this odd admiration for someone I barely knew. Your calm energy stayed with me long after we parted ways.",
    
    "Slide 4: Casual Cool\nWe talked briefly, nothing deep, just small conversation. You spoke clearly, confidently, casually. Every word felt natural. I liked that about you. There was no pressure, no need to impress anyone, yet it felt right. It was easy being around you, just one short encounter, yet your presence left a small mark. You were effortlessly correct, effortlessly cool, and I found myself replaying that conversation days later, smiling at how simple it all was.",
    
    "Slide 5: The Walk Away\nWhen you left, you didn’t look back. You didn’t dramatize the moment. You simply walked, composed, nonchalant. I liked that. I wanted to remember it all — how you moved, how you were calm, how everything felt natural. It was just one meeting, yet it left an impression. Your quiet confidence is rare. Even a brief moment can teach someone a lot about simplicity and being grounded.",
]

# Dynamically repeat slides to reach 15 if needed
while len(slides) < 15:
    slides.append(slides[-1] + " (continued)")

# Background images (repeat if fewer than slides)
images = [
    "https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1600&q=80",
]
slide_images = [images[i % len(images)] for i in range(len(slides))]

# ---------------- Session State ----------------
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "attempts" not in st.session_state: st.session_state.attempts = 0
if "locked" not in st.session_state: st.session_state.locked = False
if "current_slide" not in st.session_state: st.session_state.current_slide = 0
if "comments" not in st.session_state: st.session_state.comments = [""] * len(slides)

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
    idx = st.session_state.current_slide

    # Slide display
    st.markdown(
        f"""
        <div style="
            background-image: url('{slide_images[idx]}');
            background-size: cover;
            background-position: center;
            padding: 80px;
            border-radius: 15px;
        ">
            <div class="slide-text">
                {slides[idx].replace('\n','<br>')}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Spotify embed
    st.markdown(
        """
        <iframe style="border-radius:12px"
            src="https://open.spotify.com/embed/track/4guQztGKAETkvuTekNeqBe"
            width="300" height="80" frameborder="0"
            allow="encrypted-media; autoplay" allowfullscreen>
        </iframe>
        """,
        unsafe_allow_html=True
    )

    # Navigation and comments
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        if st.button("⬅ Previous") and st.session_state.current_slide > 0:
            st.session_state.current_slide -= 1
    with col2:
        comment = st.text_area("Leave a comment:", value=st.session_state.comments[idx], key=f"comment_{idx}")
        if st.button("Submit Comment", key=f"submit_{idx}"):
            st.session_state.comments[idx] = comment
            st.success("Comment saved 💌")
    with col3:
        if st.button("Next ➡") and st.session_state.current_slide < len(slides) - 1:
            st.session_state.current_slide += 1

    # Logout
    show_logout()
