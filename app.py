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

    st.markdown("<div class='title'>💖 Happy Birthday Dear 💖</div>", unsafe_allow_html=True)
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
with tab4:

    import time

    st.markdown("""
    <style>
    .title {
        text-align:center;
        font-size:45px;
        color:#ff4d6d;
        text-shadow:0px 0px 20px #ff4d6d;
    }

    .sub {
        text-align:center;
        color:white;
        opacity:0.8;
    }

    .box {
        display:flex;
        justify-content:center;
        margin-top:20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>📸 Memories Universe</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Smooth rotating memories ✨</div>", unsafe_allow_html=True)

    images = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]

    # 🎵 MUSIC
    try:
        audio = open("song.mp3", "rb")
        st.audio(audio.read(), format="audio/mp3")
    except:
        st.warning("Add song.mp3 🎵")

    placeholder = st.empty()

    # ================= SMOOTH ROTATION =================
    i = 0

    # keeps running visually smooth (controlled loop)
    for _ in range(20):

        with placeholder.container():

            st.markdown("<div class='box'>", unsafe_allow_html=True)

            st.image(
                images[i],
                width=420,
                caption=f"💖 Memory {i+1}"
            )

            st.markdown("</div>", unsafe_allow_html=True)

        time.sleep(2.5)   # ⏳ SLOW & SMOOTH TRANSITION
        i = (i + 1) % len(images)

    st.success("💖 Memories loaded successfully ✨")

    import streamlit as st

    images = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]

    st.markdown("""
    <style>

    /* 🌌 STAR BACKGROUND */
    body {
        overflow-x: hidden;
    }

    .stars {
        position: fixed;
        width: 100%;
        height: 100%;
        background: black;
        z-index: -1;
    }

    .stars:before {
        content: "";
        position: absolute;
        width: 200%;
        height: 200%;
        background: transparent url("https://raw.githubusercontent.com/VincentGarreau/particles.js/master/demo/media/stars.png") repeat;
        animation: moveStars 120s linear infinite;
        opacity: 0.4;
    }

    @keyframes moveStars {
        from {transform: translateY(0px);}
        to {transform: translateY(-1000px);}
    }

    /* 💖 TITLE */
    .title {
        text-align:center;
        font-size:45px;
        color:#ff4d6d;
        text-shadow:0px 0px 20px #ff4d6d;
    }

    /* 🎡 INFINITE CAROUSEL */
    .carousel {
        display: flex;
        gap: 20px;
        width: max-content;
        animation: scroll 18s linear infinite;
    }

    .carousel img {
        width: 300px;
        height: 300px;
        border-radius: 20px;
        box-shadow: 0px 0px 20px rgba(255,0,100,0.5);
        transition: transform 0.3s;
        cursor: pointer;
    }

    .carousel img:hover {
        transform: scale(1.1);
    }

    .carousel-wrapper {
        overflow: hidden;
        width: 100%;
        margin-top: 20px;
    }

    @keyframes scroll {
        0% {transform: translateX(0);}
        100% {transform: translateX(-50%);}
    }

    /* ✨ POLAROID */
    .polaroid {
        background:white;
        padding:10px;
        border-radius:10px;
        box-shadow:0px 0px 20px rgba(0,0,0,0.3);
        display:inline-block;
        transform: rotate(-2deg);
        margin:10px;
    }

    /* 🎆 FIREWORK CANVAS */
    canvas {
        position: fixed;
        top: 0;
        left: 0;
        pointer-events: none;
        z-index: 999;
    }

    </style>

    <div class="stars"></div>

    <div class="title">📸 Memories Universe PRO</div>

    """, unsafe_allow_html=True)

    # 🎵 MUSIC
    try:
        audio = open("song.mp3", "rb")
        st.audio(audio.read(), format="audio/mp3")
    except:
        st.warning("Add song.mp3 🎵")

    # ================= INFINITE CAROUSEL =================
    st.markdown("""
    <div class="carousel-wrapper">
        <div class="carousel">
            <img src="img1.jpg">
            <img src="img2.jpg">
            <img src="img3.jpg">
            <img src="img4.jpg">

            <!-- duplicate for infinite loop feel -->
            <img src="img1.jpg">
            <img src="img2.jpg">
            <img src="img3.jpg">
            <img src="img4.jpg">
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ================= POLAROID GALLERY =================
    st.markdown("### ✨ Floating Memories")

    cols = st.columns(2)

    for i in range(4):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="polaroid">
                <img src="{images[i]}" width="160">
                <p style="text-align:center;">💖 Memory {i+1}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # ================= CLICK POPUP VIEWER =================
    st.markdown("### 🧠 Click Memory Viewer")

    selected = st.radio("Choose Memory", ["1", "2", "3", "4"])

    st.image(images[int(selected)-1], width=400)

    st.success("💖 Memory opened in focus mode ✨")

    # ================= FIREWORKS CANVAS =================
    st.markdown("""
    <canvas id="fireworks"></canvas>

    <script>
    const canvas = document.getElementById("fireworks");
    const ctx = canvas.getContext("2d");

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let particles = [];

    function createFirework() {
        for (let i = 0; i < 50; i++) {
            particles.push({
                x: canvas.width/2,
                y: canvas.height/2,
                vx: (Math.random()-0.5)*8,
                vy: (Math.random()-0.5)*8,
                life: 100
            });
        }
    }

    function animate() {
        ctx.fillStyle = "rgba(0,0,0,0.1)";
        ctx.fillRect(0,0,canvas.width,canvas.height);

        particles.forEach((p, i) => {
            p.x += p.vx;
            p.y += p.vy;
            p.life--;

            ctx.fillStyle = "yellow";
            ctx.fillRect(p.x, p.y, 3, 3);

            if(p.life <= 0) particles.splice(i,1);
        });

        requestAnimationFrame(animate);
    }

    createFirework();
    animate();

    setInterval(createFirework, 3000);
    </script>
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