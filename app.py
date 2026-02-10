import streamlit as st

# ---------------- Slides Content ----------------
slides = [
    """💔 Slide 1: Memories of You
I still remember the first time our paths crossed, the way your laughter echoed in my mind long after you left. Nights feel colder now, the silence louder, and I walk through memories that burn like fire. Every song reminds me of us, every street corner a shadow of what we had. I wonder if you think of me too, or if the world moved on while I remained trapped in moments I cannot reclaim. Sometimes I close my eyes and see your face, the anime sunsets we once watched, the promises we whispered. Yet here I am, breathing through the pain, learning to stand again.""",

    """💔 Slide 2: Lonely Streets
Walking alone, streets empty, I hear echoes of our conversations in the wind. The city lights blur like tears running down a river of memories. Kiswahili songs play softly in my headphones, reminding me of the nights we stayed awake, planning a future that now feels impossible. I remember your smile, your touch, and the anime scenes we used to quote. I feel the weight of silence pressing down, yet there is a strange beauty in this solitude. Every step I take is a reminder: healing is slow, and the heart carries both the scars and the hope.""",

    """💔 Slide 3: Letters I Never Sent
I wrote words I never had the courage to say, pouring my soul into letters I never sent. Each line carried my longing, my anger, my love, and my regret. In the quiet of my room, I read them to myself, letting the ink speak what my lips could not. The pain of absence lingers, and even anime heroes’ courage feels insufficient to mend this wound. I remember our shared laughter and the music that played in the background, the Kiswahili melodies that reminded me of home and of you. The letters remain, silent witnesses to a love lost but never forgotten.""",

    """💔 Slide 4: Shadows of Your Voice
Even now, I hear your voice in the rustling leaves, the hum of a distant train, and the quiet of my apartment. Your laughter echoes like an anime soundtrack, bittersweet and haunting. Kiswahili phrases slip through my mind: 'Nakukumbuka kila siku,' I whisper, and the memory of your eyes pierces through the shadows. Nights are long, and my pillow carries your absence like a heavy stone. I am learning to speak to myself kindly, to cradle my broken heart while the world moves on. Still, some nights, I let the tears come, honoring the love that was.""",

    """💔 Slide 5: The Anime Sky
I remember us staring at sunsets that looked like anime skies, painted in shades of fire and gold. We shared dreams, whispered secrets, and imagined worlds where pain did not exist. Now, those skies feel empty without you. Every orange and pink reminds me of laughter, soft touches, and promises that faded. Kiswahili songs hum in the background of my mind: 'Nakumiss sana,' I murmur. Even in solitude, I chase hope, believing that life will offer a sky just as beautiful, even if we never share it again. The memories are sharp yet comforting, like bittersweet melodies of a song.""",

    """💔 Slide 6: Quiet Nights
Nights are hardest. The city sleeps, but my mind races. I think of you, of the words left unsaid, of hugs that never came. Anime scenes flash before my eyes, lovers separated by fate, heroes fighting pain—mirroring my own heart. I whisper Kiswahili lyrics under my breath: 'Wewe ni wa milele,' but I know you are gone. Still, I walk through the silence, learning to breathe with the absence. Every star above reminds me that even in darkness, there is beauty, and in pain, there is growth.""",

    """💔 Slide 7: Rain and Remembrance
Rain taps against my window, a rhythm that echoes my heartbeats. I remember running through puddles with you, laughing, drenched and free. Now the rain feels heavy, dragging memories along. Anime rain scenes flash in my mind—heroes standing alone, hearts shattered, but still standing. Kiswahili songs speak to me of longing: 'Nakukosa kila wakati.' I close my eyes and let the drops carry away some of the grief, hoping the heart learns slowly to love itself again while treasuring what was.""",

    """💔 Slide 8: Music and Pain
Every song I hear seems to carry your voice, the echo of moments we shared. Melodies twist through my chest, and Kiswahili lyrics remind me of streets we walked together. I play the songs from anime soundtracks, feeling the characters’ pain align with mine. I realize that heartbreak is universal, that even heroes endure loss. I write, I breathe, I remember, and slowly, I learn that pain can coexist with hope. The music becomes my companion, carrying my grief, my longing, and a quiet courage to keep moving forward.""",

    """💔 Slide 9: Letters to the Wind
I speak to the wind now, sending letters that drift where you might never read them. Each word carries my love, my regret, my anger, and my hope. Anime landscapes float through my imagination: vast skies, endless oceans, heroes seeking their paths. I whisper Kiswahili words, 'Nakumiss sana,' and feel the wind answer back in its own way. Pain is sharp, yet the act of speaking, even to nothing, brings relief. I am learning that some love exists quietly, unseen, and that memories are both a burden and a blessing.""",

    """💔 Slide 10: Fragments of Us
I collect fragments of us in my mind—the jokes, the fights, the late-night talks. They are like shattered glass, beautiful yet dangerous. Anime fragments of light and shadow echo my own heart’s turmoil. Kiswahili phrases linger: 'Nakukumbuka kila mara.' I walk through life with these shards, sometimes bleeding, sometimes smiling. Pain and love coexist, teaching me patience and courage. I understand now that love doesn’t always end in togetherness, but it leaves imprints that shape who we are.""",

    """💔 Slide 11: Silence Speaks
Sometimes, silence speaks louder than words. I hear it in the empty apartment, in the muted streets, in my own heart. Anime scenes of quiet reflection mirror me, and Kiswahili whispers rise: 'Nakukosa kweli.' I realize heartbreak is not just pain; it is understanding, growth, and patience. I let myself feel, fully and without shame, knowing each tear waters a seed of hope. The silence becomes a canvas where memories paint both sorrow and strength.""",

    """💔 Slide 12: Longing and Hope
Even in longing, there is hope. I imagine anime skies where light breaks through dark clouds, where heroes find courage in despair. I whisper Kiswahili words to myself: 'Kila kitu kitakuwa sawa.' I remember our laughter, our closeness, and I carry it forward. The heart aches, but it also learns resilience. Love may fade, but the lessons, the beauty, the memories—they remain. I am learning to hold pain gently, letting it teach me strength and compassion.""",

    """💔 Slide 13: Walking Forward
I walk forward now, even with pieces of you still inside me. Anime characters rise after heartbreak, and I rise too. Kiswahili melodies hum in my ears: 'Nakumiss, lakini lazima niende mbele.' The streets are mine to claim, the nights mine to conquer. The love we had is a memory, but it fuels my journey. I carry courage, strength, and tenderness, ready to face new days. Heartbreak has not broken me—it has shaped me.""",

    """💔 Slide 14: Stars and Reflection
Under the stars, I reflect on all we were. Anime skies shimmer like memories, Kiswahili lyrics echo softly: 'Nakukumbuka daima.' Pain mixes with gratitude, sorrow with understanding. I see the path behind me, the journey of healing, the echoes of laughter. Each star reminds me that even darkness has beauty, that heartbreak carries wisdom. I breathe, I remember, I honor what we had while embracing what comes next.""",

    """💔 Slide 15: A New Dawn
The sun rises on a world that feels different, yet familiar. Anime mornings glimmer with hope, Kiswahili songs fill my heart: 'Sasa ni wakati wa kuanza upya.' I take a deep breath and step forward. The past remains, but it no longer controls me. Heartbreak is part of life, part of love, and part of growing. I carry lessons, memories, and strength, ready to face the future with courage, hope, and a heart open to new stories."""
]

# ---------------- Streamlit Slide Logic ----------------
if "current_slide" not in st.session_state:
    st.session_state.current_slide = 0

st.title("💔 Heartbreak Slides")

# Show current slide
st.markdown(slides[st.session_state.current_slide])

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅ Previous"):
        if st.session_state.current_slide > 0:
            st.session_state.current_slide -= 1
with col2:
    if st.button("Next ➡"):
        if st.session_state.current_slide < len(slides) - 1:
            st.session_state.current_slide += 1

