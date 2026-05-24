import streamlit as st
import requests

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NeuroCampus",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

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
    padding-bottom:2rem;
}

/* LOGO HEADER */

.logo-title{
    font-size:32px;
    font-weight:900;
    color:white;
    margin-bottom:0px;
}

.logo-sub{
    color:#94a3b8;
    font-size:15px;
    margin-top:-5px;
    margin-bottom:30px;
}

/* LEFT SIDE */

.hero-title{
    font-size:62px;
    font-weight:900;
    line-height:1.1;
    color:white;
    margin-bottom:20px;
}

.hero-sub{
    color:#94a3b8;
    font-size:20px;
    margin-bottom:35px;
    line-height:1.7;
}

/* CARD */

.glass-card{
    background:rgba(17,24,39,0.7);
    backdrop-filter:blur(14px);

    padding:40px;
    border-radius:28px;

    border:1px solid rgba(255,255,255,0.08);

    box-shadow:
    0px 0px 30px rgba(0,0,0,0.35);
}

/* BUTTON */

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

    font-size:17px;

    font-weight:700;

    transition:0.3s;
}

.stButton > button:hover{

    transform:scale(1.02);

    background:
    linear-gradient(
        90deg,
        #1d4ed8,
        #6d28d9
    );
}

/* INPUTS */

.stTextInput input{

    background:#0f172a !important;
    color:white !important;

    border-radius:12px !important;
}

/* SELECT */

.stSelectbox div[data-baseweb="select"]{

    background:#0f172a !important;
    border-radius:12px !important;
}

/* TABS */

button[data-baseweb="tab"]{

    font-size:16px;
    font-weight:700;
}

/* CHATBOT FLOAT BUTTON */

.chat-btn{

    position:fixed;

    bottom:25px;

    right:25px;

    width:75px;

    height:75px;

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

    font-size:36px;

    color:white;

    text-decoration:none;

    box-shadow:
    0px 0px 25px rgba(37,99,235,0.45);

    z-index:99999;

    transition:0.3s;
}

.chat-btn:hover{

    transform:scale(1.08);

    box-shadow:
    0px 0px 35px rgba(124,58,237,0.55);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "admin" not in st.session_state:
    st.session_state.admin = False

# =========================================================
# TOP HEADER
# =========================================================

logo_col, text_col = st.columns([1,5])

with logo_col:

    st.image(
        "assets/logo.png",
        width=110
    )

with text_col:

    st.markdown("""
    <div style='margin-top:10px;'>

    <div class='logo-title'>
    NeuroCampus
    </div>

    <div class='logo-sub'>
    By ModelAI • AI Powered Smart Education Platform
    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# MAIN LAYOUT
# =========================================================

left, right = st.columns([1.3,1])

# =========================================================
# LEFT SIDE
# =========================================================

with left:

    st.markdown("""
    <div class='hero-title'>
    AI Powered<br>
    Student Management<br>
    System
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='hero-sub'>
    Academic Records + AI Engagement Prediction +
    Analytics Dashboard + Admin Monitoring
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
        use_container_width=True
    )

# =========================================================
# RIGHT SIDE
# =========================================================

with right:

    st.markdown(
        "<div class='glass-card'>",
        unsafe_allow_html=True
    )

    login_tab, signup_tab = st.tabs(
        ["🔐 Login", "📝 Signup"]
    )

    # =====================================================
    # LOGIN TAB
    # =====================================================

    with login_tab:

        st.subheader("Welcome Back 👋")

        role = st.selectbox(
            "Select Role",
            ["Student", "Admin"]
        )

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        # =================================================
        # LOGIN BUTTON
        # =================================================

        if st.button("Login"):

            # =============================================
            # ADMIN LOGIN
            # =============================================

            if role == "Admin":

                if (
                    email.strip() == "admin@gmail.com"
                    and password.strip() == "admin123"
                ):

                    st.session_state.logged_in = True
                    st.session_state.admin = True

                    st.success(
                        "Admin Login Successful"
                    )

                    st.switch_page(
                        "pages/admin.py"
                    )

                else:

                    st.error(
                        "Invalid Admin Credentials"
                    )

            # =============================================
            # STUDENT LOGIN
            # =============================================

            else:

                login_data = {

                    "email": email.strip(),
                    "password": password.strip()
                }

                try:

                    response = requests.post(

                        "http://127.0.0.1:8000/login",

                        json=login_data,

                        timeout=10
                    )

                    if response.status_code == 200:

                        st.session_state.logged_in = True
                        st.session_state.admin = False

                        st.success(
                            "Login Successful"
                        )

                        st.switch_page(
                            "pages/dashboard.py"
                        )

                    elif response.status_code == 401:

                        st.error(
                            "Invalid Email or Password"
                        )

                    else:

                        st.error(
                            f"Server Error: {response.text}"
                        )

                except requests.exceptions.ConnectionError:

                    st.error(
                        "Backend Server Not Running"
                    )

                except Exception as e:

                    st.error(
                        f"Error: {str(e)}"
                    )

    # =====================================================
    # SIGNUP TAB
    # =====================================================

    with signup_tab:

        st.subheader("Create Account 🚀")

        name = st.text_input(
            "Full Name"
        )

        signup_email = st.text_input(
            "Signup Email"
        )

        signup_password = st.text_input(
            "Signup Password",
            type="password"
        )

        if st.button("Create Account"):

            signup_data = {

                "name": name.strip(),
                "email": signup_email.strip(),
                "password": signup_password.strip()
            }

            try:

                response = requests.post(

                    "http://127.0.0.1:8000/users",

                    json=signup_data,

                    timeout=10
                )

                if response.status_code == 200:

                    st.success(
                        "Signup Successful!"
                    )

                else:

                    st.error(
                        response.text
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Backend Server Not Running"
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# =========================================================
# SHIKSHA AI FLOATING BUTTON
# =========================================================

st.markdown("""
<a href="/shiksha_ai" target="_self">
    <div class="chat-btn">
        🤖
    </div>
</a>
""", unsafe_allow_html=True)