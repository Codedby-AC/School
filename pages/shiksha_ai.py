import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from services.ai_engine import ask_shiksha_ai

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Shiksha AI",
    page_icon="🤖",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

[data-testid="stSidebar"]{
    display:none;
}

.main{
    background:
    linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #111827
    );
}

.block-container{
    padding-top:2rem;
}

.chat-card{

    background:#111827;

    padding:30px;

    border-radius:24px;

    border:1px solid rgba(255,255,255,0.08);
}

.user-box{

    background:#2563eb;

    padding:15px;

    border-radius:15px;

    margin-top:15px;

    color:white;
}

.ai-box{

    background:#1e293b;

    padding:15px;

    border-radius:15px;

    margin-top:15px;

    color:white;
}

.title{

    font-size:52px;

    font-weight:900;

    color:white;
}

.subtitle{

    color:#94a3b8;

    font-size:18px;

    margin-bottom:25px;
}

.stButton > button{

    width:100%;

    background:
    linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );

    color:white;

    border:none;

    padding:14px;

    border-radius:14px;

    font-size:16px;

    font-weight:700;
}
    
            
/* CHATBOT FLOAT BUTTON */

.chatbot-btn{

    position:fixed;

    bottom:25px;

    right:25px;

    width:70px;

    height:70px;

    border-radius:50%;

    background:
    linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
    );

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:34px;

    color:white;

    cursor:pointer;

    z-index:99999;

    box-shadow:
    0px 0px 25px rgba(37,99,235,0.45);

    transition:0.3s;
}

.chatbot-btn:hover{

    transform:scale(1.08);
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SESSION
# ==================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==================================================
# HEADER
# ==================================================

col1, col2 = st.columns([1,5])

with col1:

    st.image(
        "assets/logo.png",
        width=90
    )

with col2:

    st.markdown("""
    <div class='title'>
    🤖 Shiksha AI
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='subtitle'>
    Your Personal AI Study Assistant
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# CHAT UI
# ==================================================

st.markdown(
    "<div class='chat-card'>",
    unsafe_allow_html=True
)

user_input = st.text_area(
    "Ask Anything..."
)

if st.button("Ask AI"):

    if user_input:

        answer = ask_shiksha_ai(user_input)

        st.write(answer)
# ==================================================
# CHAT HISTORY
# ==================================================

for sender, msg in st.session_state.messages:

    if sender == "You":

        st.markdown(
            f"<div class='user-box'><b>You:</b><br>{msg}</div>",
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"<div class='ai-box'><b>Shiksha AI:</b><br>{msg}</div>",
            unsafe_allow_html=True
        )

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# =========================================================
# SHIKSHA AI FLOATING BUTTON
# =========================================================

st.markdown(
    """
    <style>
    .floating-btn{

        position:fixed;

        bottom:25px;

        right:25px;

        z-index:99999;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([8,1,1])

with col3:

    if st.button("🤖"):

        st.switch_page(
            "pages/shiksha_ai.py"
        )