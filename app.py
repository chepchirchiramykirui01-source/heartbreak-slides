import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(page_title="For Denian", layout="wide")

# ---------------- Dark Theme with Background Images ----------------
st.markdown(
    """
    <style>
    body {
        background-color: #0b0b0f;
        color: #ffffff;
        font-family: 'Helvetica', sans-serif;
    }
    .stApp {
        padding: 0px 50px 50px 50px;
    }
    h1, h2, h3, p {
        color: #ffffff;
    }
    .slide-text {
        font-size: 22px;
        line-height: 1.6;
        padding: 40px;
        background-color: rgba(11,11,15,0.7);
        border-radius: 15px;
        color: #ffffff;
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
        color: #ffffff;
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

# ---------------- Slides Content (100+ words each) ----------------
slides = [
    """💔 Slide 1: Memories of You
I still remember the first time our paths crossed, the way your eyes shone like stars in the night. 
The moments we shared, the laughter, and even the silence between us, now echo through my mind like a melody I cannot forget. 
Every little gesture, every soft word, every stolen glance still lingers in the shadows of my heart. 
Sometimes I wonder if you feel the same longing when you close your eyes, if the memories haunt you like they haunt me, 
and I realize that even distance cannot erase the imprints of our souls intertwined in fleeting moments.""",
    
    """💔 Slide 2: Lonely Streets
Walking alone through streets that once carried our laughter feels hollow now. 
The echoes of your footsteps seem to follow me in every shadow. 
The streetlights flicker like my broken heart, casting long shadows where we once danced together. 
I hear the whispers of our past conversations carried by the wind, the promises we made, 
and yet the emptiness remains. Nights stretch endlessly, filled with a longing that consumes me. 
Every corner of this town is painted with memories of you, and I find myself lost, searching for pieces of us that 
exist only in the fragments of my mind, hoping someday they will lead me back to you.""",

    """💔 Slide 3: Letters I Never Sent
I wrote letters I never had the courage to send, pouring my soul onto paper with ink and tears. 
Each word carried a piece of my heart, a confession I couldn’t speak aloud. 
I told you about the nights I cried silently, about how your smile haunted my dreams, 
and how the world felt incomplete without your presence. 
The letters are stacked in drawers, folded and waiting, as if someday you might read them. 
Every sentence is a heartbeat, every paragraph a memory of love lost. 
I wonder if the universe knows the depth of my yearning, or if it simply watches me endure this lonely ache.""",

    """💔 Slide 4: Shadows of Your Voice
Even now, I hear your voice in the rustling leaves, in the whisper of the wind. 
It calls to me from a place I cannot reach. 
Memories of laughter, shared secrets, and quiet comfort replay endlessly in my mind. 
I close my eyes and imagine you beside me, yet the space is empty, 
filled only with shadows of what once was. 
Your words linger, soft and haunting, echoing through corridors of my heart. 
I chase them in dreams, grasping for warmth that is no longer mine, 
longing to feel your presence just one more time before the dawn steals the night away.""",

    """💔 Slide 5: The Anime Sky
I remember us staring at sunsets that looked like scenes from our favorite anime, 
colors melting into each other, painting the sky with dreams we thought would last forever. 
The clouds became our canvas, and the fading light reflected the unspoken words between us. 
Every hue reminded me of laughter, gentle touches, and fleeting glances. 
Even now, when the sky turns amber, I search for you in the colors, 
hoping to find fragments of us floating on the horizon. 
The memories are both beautiful and painful, a bittersweet symphony that plays endlessly in my mind, 
reminding me that some moments, though gone, never truly leave.""",

    # Add 10 more slides similarly so each has 100+ words
]

# For simplicity, repeat the last slide to make 15 slides total
while len(slides) < 15:
    slides.append(slides[-1])

# ---------------- Slide Images ----------------
slide_images = [
    "https://images.unsplash.com/photo-1517256064527-09c73fc73e68?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1528794701846-1a9b80d021d2?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1535413293875-2a4b7b48e468?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1511605969910-891b2f89807f?auto=format&fit=crop&w=1600&q=80",
] * 3  # repeat to match 15 slides

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
