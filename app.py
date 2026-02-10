import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(page_title="For Denian", layout="wide")

# ---------------- Dark Black & Grey Theme ----------------
st.markdown(
    """
    <style>
    body {background-color: #0b0b0f; color: #ffffff; font-family: 'Helvetica', sans-serif;}
    .stApp {padding: 50px;}
    .slide-text {font-size:22px; line-height:1.6; padding:40px; 
                 background: linear-gradient(135deg, #1c1c27, #000000); 
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

# ---------------- Slides ----------------
slides = [
    "Slide 1: The Waterfall Meeting\nThat afternoon by the waterfall is burned into my memory. The sound of rushing water, sunlight reflecting on the mist, and you casually scrolling through your phone. You didn’t try to impress; you didn’t act like it was a big deal. Yet somehow, every little gesture of yours — the way you looked around, your calm presence, that slight smirk — made you seem effortlessly right. I liked it. That one brief encounter left a mark I often replay in my mind.",
    
    "Slide 2: Observing You\nI noticed small details — the tilt of your head, the relaxed way you held your phone, your calm composure as you looked at the waterfall. You didn’t speak much, but everything you did seemed naturally right. There was a quiet coolness in your presence, a nonchalant charm that drew my attention. It’s remarkable how one short meeting could make such a strong impression. Your subtle confidence and effortless demeanor are things I still think about today.",
    
    "Slide 3: My Apology\nI realize now I may have seemed overprotective or overly cautious, and I just want to apologize. I admired your calm, self-assured nature and perhaps I overthought things in my mind because I wanted to treasure that one small moment. You were effortlessly cool, and I shouldn’t have let my own worries overshadow the simplicity of what happened. My caution wasn’t about doubting you, it was about valuing that brief encounter. I’m sorry if it came off differently than I intended.",
    
    "Slide 4: Calm Presence\nEven though we only met once, your calm energy left a lasting impression. You walked with your phone, naturally composed, without exaggeration or pretense. Your presence was steady, quietly confident, and strikingly authentic. I liked everything about it. That brief afternoon at the waterfall feels vivid, as if the memory of your nonchalant charm is permanently etched in my mind. There’s a rare appeal in someone who doesn’t need to perform to leave an impression.",
    
    "Slide 5: One Meeting, Lasting Impression\nIt’s amazing how one short encounter could leave such a memorable impact. The waterfall, the light, and your casual walk with your phone — all remain in my thoughts. Your nonchalance, cool confidence, and natural authenticity made that day unforgettable. It wasn’t dramatic or overly emotional, just quietly impressive. I’ll remember that afternoon, appreciating the effortless charm and calm energy you displayed in that one perfect, fleeting moment."
]

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
        <div style="position:relative;">
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

