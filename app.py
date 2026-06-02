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
    import base64

    st.markdown("""
    <style>

    .title {
        text-align:center;
        font-size:55px;
        color:#ff4d6d;
        text-shadow:0px 0px 25px #ff4d6d;
        font-weight:bold;
    }

    .sub {
        text-align:center;
        color:white;
        opacity:0.9;
        font-size:20px;
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
        """
        <div class='sub'>
        ✨ Every picture tells a story, every memory holds a feeling 💖
        </div>
        """,
        unsafe_allow_html=True
    )

    # ================= AUTOPLAY MUSIC =================
    try:
        with open("memories_song.mp3", "rb") as f:
            audio_bytes = f.read()

        audio_base64 = base64.b64encode(audio_bytes).decode()

        st.markdown(
            f"""
            <audio autoplay loop controls>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True
        )

    except:
        st.warning("🎵 Add memories_song.mp3 beside app.py")

    # ================= IMAGES =================
    images = [
        "img1.jpg",
        "img2.jpg",
        "img3.jpg",
        "img4.jpg",
        "img5.jpg",
        "img6.jpg",
        "img7.jpg",
        "img8.jpg",
        "img9.jpg",
        "img10.jpg",
        "img11.jpg",
        "img12.jpg"
    ]

    valid_images = [img for img in images if os.path.exists(img)]

    if len(valid_images) == 0:

        st.error("❌ No images found.")
        st.info("Add your photos beside app.py")

    else:

        # ================= SLIDESHOW =================
        st.markdown("---")
        st.markdown("## 🌟 Memories Slideshow")

        slideshow = st.empty()

        for i in range(len(valid_images)):

            with slideshow.container():

                st.image(
                    valid_images[i],
                    width=650,
                    caption=f"💖 Memory {i+1}"
                )

            time.sleep(2)

        st.success("✨ Memories Loaded Successfully")

        # ================= MEMORY COLLECTION =================
        st.markdown("---")
        st.markdown("## 💕 Memory Collection")

        memory_sections = [
            ("📸 Childhood Memories", ["img1.jpg", "img2.jpg"]),
            ("💕 Favorite Moments", ["img3.jpg", "img4.jpg"]),
            ("🌸 Beautiful Smiles", ["img5.jpg", "img6.jpg"]),
            ("✨ Special Days", ["img7.jpg", "img8.jpg"]),
            ("🎂 Birthday Memories", ["img9.jpg", "img10.jpg"]),
            ("💖 Forever Memories", ["img11.jpg", "img12.jpg"])
        ]

        for title, imgs in memory_sections:

            st.markdown(f"### {title}")

            col1, col2 = st.columns(2)

            with col1:
                if os.path.exists(imgs[0]):
                    st.image(imgs[0], use_container_width=True)

            with col2:
                if os.path.exists(imgs[1]):
                    st.image(imgs[1], use_container_width=True)

        # ================= MEMORY VIEWER =================
        st.markdown("---")
        st.markdown("## 🧠 Memory Viewer")

        selected = st.selectbox(
            "Choose Your Favorite Memory 💖",
            valid_images
        )

        st.image(
            selected,
            width=750,
            caption="✨ Special Memory"
        )

        st.success("💖 Memory Opened Successfully")

        # ================= MEMORY WALL =================
        st.markdown("---")
        st.markdown("## 🌹 Memory Wall")

        cols = st.columns(3)

        for i, img in enumerate(valid_images):

            with cols[i % 3]:

                st.image(
                    img,
                    caption=f"💖 Memory {i+1}",
                    use_container_width=True
                )

        # ================= SPECIAL MESSAGE =================
        st.markdown("---")

        st.markdown("""
        <div class="memory-box">

        <h2 style="text-align:center;color:#ff4d6d;">
        💖 A Journey of Memories 💖
        </h2>

        <p style="
        text-align:center;
        color:white;
        font-size:19px;
        line-height:1.9;
        ">

        Every picture here is more than just an image. ✨

        <br><br>

        It is a memory,
        a smile,
        a beautiful moment frozen in time.

        <br><br>

        Some memories make us laugh,
        some make us emotional,
        but all of them remind us how precious certain people are. 💕

        <br><br>

        Today is not just another day.

        <br><br>

        It is a celebration of your existence,
        your smile,
        and the happiness you bring into the lives of others. 🎂✨

        <br><br>

        Happy Birthday 💖

        <br><br>

        May every memory ahead be even more beautiful than the ones collected here.

        </p>

        </div>
        """, unsafe_allow_html=True)

        st.balloons()

        st.success("🎂✨ Happy Birthday! ✨🎂")
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
