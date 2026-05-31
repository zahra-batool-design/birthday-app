import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="Birthday Surprise", layout="wide")

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🏠 Home", "❤️ Heart", "💌 Letter", "📸 Memories", "🎉 Birthday"]
)

# ===================== HOME =====================
with tab1:

    st.markdown(
        """
        <style>

        .stApp {
            background: linear-gradient(135deg, #000000, #1a001a, #000000);
        }

        .title {
            text-align: center;
            font-size: 60px;
            font-weight: bold;
            color: #ff2e63;
            text-shadow: 0px 0px 25px #ff2e63;
            margin-top: 40px;
        }

        .subtitle {
            text-align: center;
            font-size: 22px;
            color: white;
            opacity: 0.8;
        }

        .card {
            background: rgba(255,255,255,0.05);
            padding: 30px;
            border-radius: 20px;
            width: 60%;
            margin: auto;
            margin-top: 40px;
            text-align: center;
            box-shadow: 0px 0px 25px rgba(255,46,99,0.3);
            backdrop-filter: blur(10px);
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='title'>💖 Happy Birthday  💖</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>A special surprise is waiting for you ✨</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("### 🎂 Wishes for you:")
    st.markdown("✨ Happiness")
    st.markdown("✨ Success")
    st.markdown("✨ Love")
    st.markdown("✨ Peace")

    st.markdown("</div>", unsafe_allow_html=True)


# ===================== HEART =====================
with tab2:

    st.markdown(
        "<h1 style='text-align:center;color:red;text-shadow:0px 0px 20px red;'>❤️ Happy Birthday Dear ❤️</h1>",
        unsafe_allow_html=True
    )

    # 🎵 MUSIC
    try:
        audio_file = open("song.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")
    except:
        st.warning("🎵 Add song.mp3 in same folder")

    placeholder = st.empty()

    for frame in range(60):

        x_list = []
        y_list = []

        for i in range(0, 360, 2):
            angle = np.radians(i)

            x = 16 * (np.sin(angle))**3
            y = (13 * np.cos(angle)
                 - 5 * np.cos(2 * angle)
                 - 2 * np.cos(3 * angle)
                 - np.cos(4 * angle))

            x *= 10
            y *= 10

            scale = 1 + 0.12 * np.sin(frame * 0.2)

            x *= scale
            y = y * scale + np.sin(frame * 0.3) * 5

            x_list.append(x)
            y_list.append(y)

        df = pd.DataFrame({"x": x_list, "y": y_list})

        placeholder.vega_lite_chart(
            df,
            {
                "mark": {
                    "type": "circle",
                    "color": "red",
                    "size": 90,
                    "opacity": 0.95
                },
                "encoding": {
                    "x": {"field": "x", "type": "quantitative"},
                    "y": {"field": "y", "type": "quantitative"}
                },
                "width": 700,
                "height": 600
            }
        )

        time.sleep(0.05)


# ===================== LOVE LETTER =====================
with tab3:

    st.markdown(
        """
        <style>

        .letter-title {
            text-align: center;
            font-size: 45px;
            color: #ff4d6d;
            text-shadow: 0px 0px 20px #ff4d6d;
        }

        .letter {
            background: rgba(255,255,255,0.05);
            padding: 30px;
            border-radius: 20px;
            width: 70%;
            margin: auto;
            margin-top: 30px;
            color: white;
            font-size: 18px;
            line-height: 1.8;
            box-shadow: 0px 0px 25px rgba(255,0,100,0.3);
            backdrop-filter: blur(10px);
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='letter-title'>💌 Love Letter</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='letter'>

    Dear Special One, <br><br>

    I don’t even know how to perfectly express this feeling… but you mean a lot to me. 💖  
    Slowly, unintentionally, you became someone very special in my heart.  

    I admire your smile, your presence, and the way you make everything feel better just by being there. ✨  

    Maybe I never said it clearly, but I really like you… more than just a normal thought. ❤️  

    This is not a demand or expectation… just a pure feeling from my heart.  

    <br><br>

    And lastly…  
    <b>your well wisher 💌</b>

    </div>
    """, unsafe_allow_html=True)


# ===================== MEMORIES =====================
# ===================== MEMORIES =====================
with tab4:

    import time
    import os

    st.markdown("""
    <style>

    .title {
        text-align:center;
        font-size:50px;
        color:#ff4d6d;
        text-shadow:0px 0px 25px #ff4d6d;
        font-weight:bold;
    }

    .sub {
        text-align:center;
        color:white;
        opacity:0.8;
        font-size:18px;
        margin-bottom:20px;
    }

    .memory-box {
        background: rgba(255,255,255,0.05);
        padding:25px;
        border-radius:20px;
        margin-top:20px;
        box-shadow:0px 0px 25px rgba(255,0,100,0.25);
        backdrop-filter: blur(10px);
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= TITLE =================
    st.markdown(
        "<div class='title'>📸 Memories Universe PRO</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub'>Every picture holds a beautiful memory 💖</div>",
        unsafe_allow_html=True
    )

    # ================= MUSIC =================
    try:
        with open("song.mp3", "rb") as audio:
            st.audio(audio.read(), format="audio/mp3")
    except:
        st.warning("🎵 Add song.mp3 in same folder as app.py")

    # ================= IMAGE LIST =================
    images = [
        "img1.jpg",
        "img2.jpg",
        "img3.jpg",
        "img4.jpg"
    ]

    # ================= CHECK IMAGES =================
    valid_images = []

    for img in images:
        if os.path.exists(img):
            valid_images.append(img)

    if len(valid_images) == 0:

        st.error("❌ No images found.")

        st.info("""
        Put these files beside app.py:

        img1.jpg
        img2.jpg
        img3.jpg
        img4.jpg
        """)

    else:

        # ================= SLIDESHOW =================
        st.markdown("---")
        st.markdown("## 🌟 Memories Slideshow")

        placeholder = st.empty()

        for i in range(8):

            current_img = valid_images[i % len(valid_images)]

            with placeholder.container():

                st.image(
                    current_img,
                    width=550,
                    caption=f"💖 Special Memory {i % len(valid_images) + 1}"
                )

            time.sleep(2)

        st.success("💖 Memories Loaded Successfully")

        # ================= FLOATING MEMORIES =================
        st.markdown("---")
        st.markdown("## ✨ Floating Memories")

        st.write(
            "Every picture tells a story and every story becomes a beautiful memory. 💕"
        )

        cols = st.columns(2)

        for i, img in enumerate(valid_images):

            with cols[i % 2]:

                st.image(
                    img,
                    caption=f"💖 Memory {i+1}",
                    use_container_width=True
                )

        # ================= MEMORY VIEWER =================
        st.markdown("---")
        st.markdown("## 🧠 Memory Viewer")

        selected = st.selectbox(
            "Choose a Memory",
            range(len(valid_images)),
            format_func=lambda x: f"💖 Memory {x+1}"
        )

        st.image(
            valid_images[selected],
            caption=f"✨ Memory {selected+1}",
            width=700
        )

        st.success("💖 Memory Opened Successfully")

        # ================= SPECIAL MESSAGE =================
        st.markdown("---")

        st.markdown("""
        <div class="memory-box">

        <h2 style="text-align:center;color:#ff4d6d;">
        💖 Special Memories 💖
        </h2>

        <p style="text-align:center;color:white;font-size:18px;line-height:1.8;">
        Some moments may pass,
        but the memories created from them stay forever. ✨
        <br><br>
        Every picture here is a reminder of happiness,
        laughter, beautiful times,
        and unforgettable moments. 💕
        </p>

        </div>
        """, unsafe_allow_html=True)
   # ===================== BIRTHDAY TAB =====================
with tab5:

    st.markdown("""
    <style>

    .birthday-title {
        text-align:center;
        font-size:70px;
        color:#ff2e63;
        text-shadow:0px 0px 30px #ff2e63;
        margin-top:40px;
        animation: glow 2s infinite alternate;
    }

    @keyframes glow {
        from {text-shadow:0px 0px 10px #ff2e63;}
        to {text-shadow:0px 0px 40px #ff2e63;}
    }

    .sub {
        text-align:center;
        color:white;
        font-size:22px;
        opacity:0.9;
    }

    /* 🎈 BALLOONS */
    .balloon {
        position: absolute;
        width: 40px;
        height: 50px;
        border-radius: 50%;
        animation: float 6s infinite ease-in-out;
        opacity: 0.8;
    }

    .balloon:nth-child(1){left:10%; background:red; animation-delay:0s;}
    .balloon:nth-child(2){left:25%; background:yellow; animation-delay:1s;}
    .balloon:nth-child(3){left:50%; background:blue; animation-delay:2s;}
    .balloon:nth-child(4){left:70%; background:pink; animation-delay:3s;}
    .balloon:nth-child(5){left:85%; background:purple; animation-delay:4s;}

    @keyframes float {
        0% {transform: translateY(100vh);}
        100% {transform: translateY(-20vh);}
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='birthday-title'>🎉 Happy Birthday 🎉</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Wishing you endless joy, love & success 💖</div>", unsafe_allow_html=True)

    # 🎈 balloons
    st.markdown("""
    <div class="balloon"></div>
    <div class="balloon"></div>
    <div class="balloon"></div>
    <div class="balloon"></div>
    <div class="balloon"></div>
    """, unsafe_allow_html=True)

    # 🎵 MUSIC
    try:
        audio = open("song.mp3", "rb")
        st.audio(audio.read(), format="audio/mp3")
    except:
        st.warning("Add song.mp3 🎵")

    # 🎆 SIMPLE FIREWORKS TEXT EFFECT
    st.markdown("""
    <div style="text-align:center; margin-top:40px; font-size:20px; color:white;">
        ✨ Let the sky shine with fireworks for you ✨
    </div>
    """, unsafe_allow_html=True)
