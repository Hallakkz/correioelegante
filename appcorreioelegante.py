import streamlit as st
import time

st.set_page_config(
    page_title="Correio Elegante 🌽",
    page_icon="🌽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── Estado ─────────────────────────────────────────────────────────────────────
if "screen" not in st.session_state:
    st.session_state.screen = 1
if "quiz_answer" not in st.session_state:
    st.session_state.quiz_answer = None
if "final_answer" not in st.session_state:
    st.session_state.final_answer = None

# ── Estilo global ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"] {
    background-color: #0d0d0d !important;
}
[data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="stSidebar"], footer, #MainMenu { display: none !important; }

.block-container { padding: 3rem 1.5rem 2rem !important; max-width: 640px !important; }

/* Tipografia */
h1 {
    font-family: 'DM Serif Display', serif !important;
    color: #f0ece4 !important;
    font-size: clamp(2rem, 6vw, 3.2rem) !important;
    line-height: 1.2 !important;
    text-align: center !important;
}
h2 {
    font-family: 'DM Serif Display', serif !important;
    font-style: italic !important;
    color: #e8b86d !important;
    font-size: clamp(1.2rem, 4vw, 1.7rem) !important;
    line-height: 1.4 !important;
    text-align: center !important;
    font-weight: 400 !important;
}
h3 {
    font-family: 'DM Sans', sans-serif !important;
    color: #a09880 !important;
    font-size: clamp(1rem, 3vw, 1.2rem) !important;
    font-weight: 300 !important;
    text-align: center !important;
    line-height: 1.7 !important;
}
p {
    font-family: 'DM Sans', sans-serif !important;
    color: #d4cfc6 !important;
    font-size: clamp(1rem, 2.8vw, 1.1rem) !important;
    line-height: 1.75 !important;
    font-weight: 300 !important;
    text-align: center !important;
}

/* Badge */
.badge {
    display: block;
    text-align: center;
    font-family: 'DM Sans', sans-serif;
    font-size: .68rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #e8b86d;
    border: 1px solid rgba(232,184,109,.3);
    border-radius: 20px;
    padding: 5px 16px;
    width: fit-content;
    margin: 0 auto 28px;
}

/* Divisor */
.div {
    width: 40px;
    height: 1px;
    background: linear-gradient(90deg,transparent,#e8b86d,transparent);
    margin: 20px auto;
}

/* Caixa resposta */
.resp {
    background: rgba(232,184,109,.06);
    border: 1px solid rgba(232,184,109,.2);
    border-radius: 16px;
    padding: 20px 28px;
    margin: 20px auto;
    font-family: 'DM Serif Display', serif !important;
    font-style: italic;
    font-size: 1.1rem !important;
    color: #e8b86d !important;
    text-align: center;
}

/* Card final */
.card {
    background: rgba(232,184,109,.06);
    border: 1px solid rgba(232,184,109,.15);
    border-radius: 20px;
    padding: 28px 36px;
    margin: 20px auto;
    text-align: center;
}

/* Espaçadores */
.gap { margin: 16px 0; }
.gap2 { margin: 32px 0; }

/* Botões Streamlit */
.stButton > button {
    background: transparent !important;
    border: 1px solid rgba(232,184,109,.5) !important;
    color: #e8b86d !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: .82rem !important;
    font-weight: 500 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    padding: 12px 32px !important;
    border-radius: 30px !important;
    transition: all .3s ease !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: rgba(232,184,109,.08) !important;
    border-color: #e8b86d !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(232,184,109,.2) !important;
}

/* Partículas */
@keyframes float1 { 0%,100%{transform:translateY(0) translateX(0)}50%{transform:translateY(-18px) translateX(8px)} }
@keyframes float2 { 0%,100%{transform:translateY(0) translateX(0)}50%{transform:translateY(-12px) translateX(-10px)} }
@keyframes float3 { 0%,100%{transform:translateY(0) translateX(0)}50%{transform:translateY(-20px) translateX(5px)} }
@keyframes fadein { from{opacity:0;transform:translateY(16px)} to{opacity:1;transform:translateY(0)} }

.particle {
    position: fixed;
    pointer-events: none;
    font-size: 1rem;
    opacity: .18;
    z-index: 0;
}
.p1{top:10%;left:8%;animation:float1 6s ease-in-out infinite;}
.p2{top:20%;right:10%;animation:float2 8s ease-in-out infinite;}
.p3{top:50%;left:5%;animation:float3 7s ease-in-out infinite;}
.p4{top:70%;right:7%;animation:float1 9s ease-in-out infinite;}
.p5{top:85%;left:20%;animation:float2 6.5s ease-in-out infinite;}
.p6{top:35%;right:4%;animation:float3 8.5s ease-in-out infinite;}
.p7{top:60%;left:15%;animation:float1 7.5s ease-in-out infinite;}
.p8{top:15%;left:40%;animation:float2 9.5s ease-in-out infinite;}
.p9{top:80%;right:25%;animation:float3 6s ease-in-out infinite;}
.p10{top:45%;right:20%;animation:float1 8s ease-in-out infinite;}

.anim { animation: fadein .8s ease both; }
.anim2 { animation: fadein .8s ease .2s both; }
.anim3 { animation: fadein .8s ease .5s both; }
.anim4 { animation: fadein .8s ease .8s both; }
.anim5 { animation: fadein .8s ease 1.1s both; }

/* Bandeirinhas */
.bunting {
    position: fixed;
    top: 0; left: 0; right: 0;
    text-align: left;
    padding: 6px 0 0 10px;
    font-size: 1.1rem;
    letter-spacing: 3px;
    z-index: 100;
    pointer-events: none;
    opacity: .55;
}
</style>

<!-- Partículas -->
<div class="particle p1">✨</div>
<div class="particle p2">🌟</div>
<div class="particle p3">⭐</div>
<div class="particle p4">✨</div>
<div class="particle p5">🌽</div>
<div class="particle p6">💫</div>
<div class="particle p7">✨</div>
<div class="particle p8">⭐</div>
<div class="particle p9">🌟</div>
<div class="particle p10">💫</div>


""", unsafe_allow_html=True)

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TELA 1
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.screen == 1:

    st.markdown('<div class="badge anim">✦ correio elegante digital ✦</div>', unsafe_allow_html=True)
    st.title("Parabéns.")
    st.markdown("<div class='gap'></div>", unsafe_allow_html=True)
    st.markdown("""
    <h3 class="anim2">
        Você encontrou o único correio elegante<br>
        programado por alguém com tempo demais 👀
    </h3>
    """, unsafe_allow_html=True)
    st.markdown("<div class='div anim3'></div>", unsafe_allow_html=True)
    st.markdown('<p class="anim4" style="color:#6b6560;font-size:.82rem!important;">role para baixo · ou clique no botão</p>', unsafe_allow_html=True)
    st.markdown("<div class='gap2'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("continuar →", key="b1"):
            st.session_state.screen = 2
            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TELA 2
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == 2:

    st.markdown('<div class="badge anim">✦ os motivos ✦</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="anim">Motivos pelos quais eu fiz isso:</h2>', unsafe_allow_html=True)
    st.markdown("<div class='div anim2'></div>", unsafe_allow_html=True)
    st.markdown("""
    <p class="anim2">
        — flores morrem<br>
        — chocolate acaba<br>
        — mas um site hospedado gratuitamente<br>
        &nbsp;&nbsp;&nbsp;dura pra sempre ✨
    </p>
    """, unsafe_allow_html=True)
    st.markdown('<p class="anim3" style="font-size:2rem!important;">🌽</p>', unsafe_allow_html=True)
    st.markdown('<p class="anim4" style="color:#6b6560;font-size:.82rem!important;font-style:italic;">sim, foi planejado. não, não me arrependo.</p>', unsafe_allow_html=True)
    st.markdown("<div class='gap2'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("ok, isso foi criativo", key="b2"):
            st.session_state.screen = 3
            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TELA 2.5 — Cutscene
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == 3:

    st.markdown('<div class="badge anim">✦ sendo honesto ✦</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="anim">E sendo sincero…</h2>', unsafe_allow_html=True)
    st.markdown("<div class='gap'></div>", unsafe_allow_html=True)
    st.markdown("""
    <p class="anim2">
        depois daquela foto de óculos e cachos,<br>
        meu cérebro decidiu perder a capacidade<br>
        de agir normalmente 😶
    </p>
    """, unsafe_allow_html=True)
    st.markdown("<div class='div anim3'></div>", unsafe_allow_html=True)
    st.markdown('<h2 class="anim3">Em minha defesa…</h2>', unsafe_allow_html=True)
    st.markdown("<div class='gap'></div>", unsafe_allow_html=True)
    st.markdown("""
    <p class="anim4">
        é difícil manter a postura<br>
        quando você aparece bonita daquele jeito 😔
    </p>
    """, unsafe_allow_html=True)
    st.markdown('<p class="anim5" style="font-size:2rem!important;margin-top:16px;">💫</p>', unsafe_allow_html=True)
    st.markdown("<div class='gap2'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("continuar →", key="b3"):
            st.session_state.screen = 4
            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TELA 3 — Quiz
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == 4:

    QUIZ = {
        "🔥 genial":                       "finalmente alguém reconhecendo meu talento.",
        "🙂 fofo":                         "objetivo alcançado 😌",
        "🤨 meio estranho":                "aceito. mas ainda assim você continuou lendo.",
        "🚨 você precisa arrumar hobbies": "justo. mas admito que funcionou porque você ainda tá aqui.",
    }

    st.markdown('<div class="badge anim">✦ o quiz ✦</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="anim">
        Desde que falei com você,<br>
        fiquei pensando em um jeito diferente<br>
        de continuar a conversa 😅
    </p>
    """, unsafe_allow_html=True)
    st.markdown("<div class='div anim2'></div>", unsafe_allow_html=True)
    st.markdown('<p class="anim2" style="font-size:.72rem!important;letter-spacing:2px;text-transform:uppercase;color:#a09880;">Escolha seu nível de aprovação desse correio elegante</p>', unsafe_allow_html=True)
    st.markdown("<div class='gap'></div>", unsafe_allow_html=True)

    if not st.session_state.quiz_answer:
        for opcao, resposta in QUIZ.items():
            if st.button(opcao, key=f"q_{opcao}", use_container_width=True):
                st.session_state.quiz_answer = resposta
                st.rerun()
    else:
        st.markdown(f'<div class="resp">"{st.session_state.quiz_answer}"</div>', unsafe_allow_html=True)
        st.markdown("<div class='gap'></div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("continuar →", key="b4"):
                st.session_state.screen = 5
                st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TELA FINAL
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == 5:

    RESPS = {
        "talvez 👀": (
            "🌽✨",
            "talvez já é mais que o suficiente pra eu chegar com um sorriso na festa.",
            "te vejo lá. prometo que chego arrumado."
        ),
        "vou pensar": (
            "😌",
            "ok, respeito o processo decisório.",
            "enquanto você pensa, estarei aqui fingindo que não tô ansioso."
        ),
    }

    st.markdown('<div class="badge anim">✦ o final ✦</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="anim">
        Se você sorriu em alguma parte,<br>
        então esse correio elegante<br>
        já valeu a pena 😌
    </p>
    """, unsafe_allow_html=True)
    st.markdown("<div class='div anim2'></div>", unsafe_allow_html=True)
    st.markdown("""
    <p class="anim2" style="margin-bottom:10px;">Mas fiquei com uma dúvida…</p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h2 class="anim3">
        depois da festa,<br>
        eu ganho um papo<br>
        ou arrisco tentar um selinho? 🌽✨
    </h2>
    """, unsafe_allow_html=True)
    st.markdown("<div class='gap2'></div>", unsafe_allow_html=True)

    if not st.session_state.final_answer:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("talvez 👀", key="fa", use_container_width=True):
                st.session_state.final_answer = "talvez 👀"
                st.rerun()
        with col3:
            if st.button("vou pensar", key="fb", use_container_width=True):
                st.session_state.final_answer = "vou pensar"
                st.rerun()
    else:
        icon, l1, l2 = RESPS[st.session_state.final_answer]
        st.markdown(f"""
        <div class="card">
            <p style="font-size:2.2rem!important;margin-bottom:14px;">{icon}</p>
            <p style="font-family:'DM Serif Display',serif!important;font-style:italic;
               color:#e8b86d!important;font-size:1.1rem!important;margin-bottom:10px;">
               "{l1}"
            </p>
            <p style="font-size:.82rem!important;color:#a09880!important;font-style:italic;">
               {l2}
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='gap2'></div>", unsafe_allow_html=True)
        st.markdown("<div class='div'></div>", unsafe_allow_html=True)
        st.markdown('<p style="font-size:.78rem!important;color:#6b6560!important;font-style:italic;margin-top:12px;">feito com 🌽 e uma dose de coragem</p>', unsafe_allow_html=True)
        st.markdown("<div class='gap'></div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("↩ recomeçar", key="restart"):
                st.session_state.screen = 1
                st.session_state.quiz_answer = None
                st.session_state.final_answer = None
                st.rerun()