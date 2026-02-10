import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(page_title="For Denian", layout="wide")

# ---------------- Dark + Anime Overlay Theme ----------------
st.markdown(
    """
    <style>
    body {background-color: #0b0b0f; color: #ffffff; font-family: 'Helvetica', sans-serif;}
    .stApp {padding: 0px 50px 50px 50px;}
    .slide-text {font-size:22px; line-height:1.6; padding:40px; 
                 background-color: rgba(11,11,15,0.7); border-radius:15px; color:#ffffff;}
    .stButton>button {background-color:#ff4b5c; color:white; border-radius:10px; padding:10px 20px; font-size:16px;}
    .stTextArea>div>textarea {background-color:#1c1c27; color:#ffffff; font-size:18px;}
    .anime-overlay {
        position: absolute;
        top:0; left:0;
        width:100%; height:100%;
        pointer-events:none;
        background-image: url('https://i.ibb.co/6mG6K9b/anime-rain-petal.png');
        background-repeat: repeat;
        opacity: 0.3;
        mix-blend-mode: lighten;
        border-radius:15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- Login Config ----------------
USERNAME = "denian"
PASSWORD = "onlyyou"
MAX_ATTEMPTS = 3

# ---------------- Slides (unique, 100+ words each) ----------------
slides = [
    "Slide 1: The Waterfall Meeting\nThat afternoon by the waterfall is burned into my memory. The sound of rushing water, sunlight reflecting on the mist, and you casually scrolling through your phone. You didn’t try to impress; you didn’t act like it was a big deal. Yet somehow, every little gesture of yours — the way you looked around, your calm presence, that slight smirk — made you seem effortlessly right. I liked it. It was just one brief encounter, but your confidence and nonchalant energy made it memorable, and I’ve thought about it often since.",
    
    "Slide 2: Observing You\nI remember the small moments, like the way you tilted your head slightly while reading a message, or how your eyes tracked the water without rushing. You didn’t speak much, yet everything you did seemed perfectly natural. There was a quiet composure about you that felt cool, like you owned the space without even trying. I kept noticing these little things silently, enjoying how real you were. Even though we only met once, your calm, collected energy left a mark that has stayed with me.",
    
    "Slide 3: The Conversation\nWe exchanged only a few words, nothing deep or serious. And yet, everything you said sounded natural, confident, and somehow perfectly right. There was no effort to impress, no exaggeration, just casual clarity in your words. I liked it. I appreciated that I could talk to you without awkwardness, that the conversation flowed easily despite being strangers. Those few lines of dialogue, your smile, and your relaxed stance made the short time we shared feel surprisingly meaningful, like a small but vivid memory etched into a day I’ll always remember.",
    
    "Slide 4: Your Energy\nIt wasn’t dramatic or overbearing, just you walking calmly, phone in hand, observing the waterfall and surroundings. There was something magnetic about how effortless you were. I liked that every move seemed intentional yet easy. Watching you, I realized how much I admired people who could be quietly confident without trying. You had this balance — composed, nonchalant, but somehow deeply memorable. One meeting, one afternoon, and I found myself replaying these subtle details, appreciating the authenticity in your demeanor without needing more.",
    
    "Slide 5: My Apology\nI realize now I may have seemed overprotective or too cautious, and I just want to apologize. I liked your calm, self-assured nature and maybe I overthought things in my mind because I wanted to hold onto the memory of that day. You were effortlessly cool, and I shouldn’t have let my own worries overshadow the simplicity of what happened. I hope you know that my caution wasn’t about doubting you, it was about treasuring that one small moment with you. I’m sorry if it came off differently than I intended.",
    
    "Slide 6: The Waterfall Sound\nEven now, when I think of that waterfall, I can hear the water crashing, feel the sunlight on the mist, and recall your relaxed stance as you scrolled through your phone. Nothing flashy, nothing exaggerated, just you being present. I liked how calm and composed you were, like you didn’t need to be anyone else. That brief impression of you feels authentic and cool. One day, one meeting, and yet your energy is something I remember vividly whenever I imagine that place.",
    
    "Slide 7: Quiet Admiration\nI admired the way you carried yourself without trying. Not flashy, not loud, just steady, calm, and confident. There’s a rare appeal in someone who doesn’t need validation yet draws attention effortlessly. I found myself quietly noticing these small traits, the way you held your phone, the way you glanced at the water, the relaxed posture. You didn’t know I was observing, yet those tiny details made a lasting impression. It’s strange how one meeting can leave such a strong, quiet memory.",
    
    "Slide 8: Little Smiles\nThere were brief smiles, little gestures that didn’t mean much in the moment but stayed with me. A glance at the waterfall, a soft laugh at something small, the slight tilt of your head — all of it felt natural and unforced. I liked how authentic it was, how comfortable you seemed being yourself. Those fleeting impressions, subtle yet powerful, made the short meeting meaningful. I still replay them in my head, appreciating the casual confidence you exuded in such a small span of time.",
    
    "Slide 9: Calm Presence\nYour calm presence was striking. You didn’t need to dominate the space or draw attention, yet everything about you seemed perfectly balanced. I liked that about you. I remember watching you for a few moments, realizing how composed and naturally right everything you did felt. It wasn’t intentional, it wasn’t calculated — it was simply who you were. That day left a lasting mark because of this, a subtle admiration for a person who makes being themselves look effortless.",
    
    "Slide 10: The Departure\nWhen the meeting ended, you walked away casually, phone in hand, not rushing, not looking back. It was natural, understated, yet memorable. I liked how confident and nonchalant you were. Even though we only met once, that one brief walk, that calm energy, made the moment stick in my mind. There was no drama, no fanfare — just authenticity. And that’s what made it so memorable for me. It’s rare to encounter someone who leaves an impression without trying, and you did.",
    
    "Slide 11: Replay in Mind\nDays later, I found myself thinking about that brief encounter. The waterfall, your casual energy, the subtle smiles — all of it plays in my mind like a short, perfect scene. I liked how relaxed and grounded you were, how effortlessly right everything you did seemed. One afternoon, one short meeting, yet it left a memory that continues to stand out. It wasn’t dramatic, it wasn’t emotional in an over-the-top way; it was real, natural, and somehow deeply memorable.",
    
    "Slide 12: Simple Confidence\nYou didn’t need words or gestures to impress. Your simple confidence was enough. I liked how you could be fully present without performing. There’s an authenticity in that which is rare. Observing you, even for a few minutes, felt like seeing someone comfortable in their own skin. I appreciated that calm energy, that quiet assurance, and how it made the moment at the waterfall feel so vivid and significant, despite being brief.",
    
    "Slide 13: Little Observations\nI noticed subtle details — the way your eyes scanned the surroundings, the natural ease in your posture, the slight tilt of your head as you read something on your phone. None of it was staged. None of it was exaggerated. And yet, it all combined into an impression I won’t forget. One brief meeting, yet so many small, lasting memories. I liked that authenticity and calmness, and it keeps replaying in my thoughts from time to time.",
    
    "Slide 14: Impact Without Words\nWe barely spoke, but your presence said everything. I liked that about you. You didn’t try to impress, yet I found myself drawn to your quiet confidence. It’s rare to encounter someone who leaves an impression without over-explaining or performing. That day at the waterfall is etched in my memory because of how naturally right and effortless you seemed. Even without drama or emotion, your energy was impactful and memorable.",
    
    "Slide 15: One Meeting, Lasting Impression\nIt’s strange that one short meeting could leave such a lasting impression. The waterfall, the sunlight, your calm walk with your phone, and the casual way you existed in that space — all of it stays with me. I liked everything about it: your nonchalance, your cool confidence, your natural presence. It wasn’t love at first sight or anything dramatic. It was simply admiration for someone effortlessly authentic. I’ll remember that day quietly, appreciating how impactful one brief encounter can be."
]

# ---------------- Dark, moody images for depression + anime overlay ----------------
slide_images = [
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1600&q=80", # dark waterfall
    "https://images.unsplash.com/photo-1529253355930-1c6211878aa2?auto=format&fit=crop&w=1600&q=80", # misty forest
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1600&q=80", # cloudy river
    "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1600&q=80", # dark rocks
    "https://images.unsplash.com/photo-1512813195386-6cf811ad3542?auto=format&fit=crop&w=1600&q=80", # gloomy lake
]
slide_images = [slide_images[i % len(slide_images)] for i in range(len(slides))]

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

    # Slide display with anime overlay
    st.markdown(
        f"""
        <div style="position:relative;">
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
                <div class="anime-overlay"></div>
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
