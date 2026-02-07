import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Vinnu ❤️ Maha", layout="wide")

# ---------- GLOBAL STYLE ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg,#fff0f3,#ffe6ea,#fff5f7);
}

.title {
    text-align:center;
    color:#e60026;
    font-size:48px;
    font-weight:bold;
}

.card {
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 6px 18px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ---------- NAVIGATION ----------
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Our Story", "Memories", "Letter", "Forgive Me"]
)

# ---------- HOME ----------
if page == "Home":
    st.markdown('<p class="title">Vinnu ❤️ Maha</p>', unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1518199266791-5375a83190b7",
        use_column_width=True
    )

    st.markdown("""
    <div class="card">
    <h3>Happy Rose Day Maha 🌹</h3>

    Some people come into life unexpectedly
    and make everything feel calmer and happier.

    Maha, you are that person in my life.

    This little website is made for you ❤️
    </div>
    """, unsafe_allow_html=True)

# ---------- STORY ----------
elif page == "Our Story":
    st.header("Our CBIT Story 📖")

    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
        use_column_width=True
    )

    st.markdown("""
    <div class="card">
    We met at CBIT.

    Started as classmates.
    Became friends during assignments and exams.

    Through studies, stress, and college life,
    we supported each other.

    And slowly, you became the most important part
    of my college journey.
    </div>
    """, unsafe_allow_html=True)

# ---------- MEMORIES ----------
elif page == "Memories":
    st.header("Little Moments I Love ❤️")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1511988617509-a57c8a288659",
            use_column_width=True
        )

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2",
            use_column_width=True
        )

    st.markdown("""
    <div class="card">
    Not just big memories —
    but small ones too.

    Study sessions together.
    Random conversations.
    Laughing for no reason.
    Supporting each other.

    Those moments mean everything to me.
    </div>
    """, unsafe_allow_html=True)

# ---------- LETTER ----------
elif page == "Letter":
    st.header("A Letter For Maha 💌")

    html("""
    <div id="letter" style="font-size:20px;"></div>

    <script>
    const text = `Dear Maha,

From CBIT classrooms to late-night study talks,
you’ve always been my strongest support.

You made difficult days easier
and happy days more meaningful.

I’m really sorry if I hurt you.

You mean so much to me.

– Vinnu ❤️`;

    let i = 0;
    function typeWriter() {
      if (i < text.length) {
        document.getElementById("letter").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter, 35);
      }
    }
    typeWriter();
    </script>
    """, height=300)

# ---------- FORGIVE ----------
elif page == "Forgive Me":
    st.header("Try Clicking the Button 😄")

    html("""
    <div style="height:300px; position:relative;">
      <button id="runaway"
      style="
        position:absolute;
        padding:15px 25px;
        background:#ff4b6e;
        color:white;
        border:none;
        border-radius:20px;
        font-size:18px;">
        Forgive Me Maha
      </button>
    </div>

    <script>
    const btn = document.getElementById("runaway");

    btn.addEventListener("mouseover", function() {
        btn.style.left = Math.random()*300 + "px";
        btn.style.top = Math.random()*200 + "px";
    });
    </script>
    """, height=350)

    st.write("Okay okay… I deserve that 😅")
