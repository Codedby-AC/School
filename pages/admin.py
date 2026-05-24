id="adminultimate"
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛡️",
    layout="wide"
)


# ---------------- LOGO HEADER ---------------- #

col_logo, col_title = st.columns([1, 5])

with col_logo:

    st.image(
        "assets/logo.png",
        width=120
    )

with col_title:

    st.markdown("""
    <div style='margin-top:15px;'>

    <h1 style='
    color:white;
    margin-bottom:0px;
    font-size:52px;
    font-weight:900;
    '>
    NeuroCampus
    </h1>

    <p style='
    color:#94a3b8;
    font-size:18px;
    '>
    By ModelAI • AI Powered Smart Education Platform
    </p>

    </div>
    """, unsafe_allow_html=True)
# =========================================================
# SECURITY
# =========================================================

if "logged_in" not in st.session_state:
    st.switch_page("frontend.py")

if not st.session_state.get("admin"):

    st.error("Unauthorized Access")
    st.stop()

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
}

.title{
    font-size:52px;
    font-weight:900;
    color:white;
    margin-bottom:10px;
}

.subtitle{
    color:#94a3b8;
    font-size:18px;
    margin-bottom:30px;
}

.metric-card{
    background:#111827;
    padding:25px;
    border-radius:22px;

    border:1px solid rgba(255,255,255,0.08);

    box-shadow:
    0px 0px 25px rgba(0,0,0,0.35);
}

.section-card{

    background:#111827;

    padding:25px;

    border-radius:22px;

    margin-top:25px;

    border:1px solid rgba(255,255,255,0.08);
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

.stButton > button:hover{

    transform:scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATABASE
# =========================================================

DATABASE_URL = "mysql+pymysql://root:123456@localhost/school"

engine = create_engine(DATABASE_URL)

students_df = pd.read_sql(
    "SELECT * FROM students",
    engine
)

progress_df = pd.read_sql(
    "SELECT * FROM progress",
    engine
)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class='title'>
🛡️ AI Powered Admin Dashboard
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Monitor Students, AI Predictions & Academic Analytics
</div>
""", unsafe_allow_html=True)

# =========================================================
# METRICS
# =========================================================

total_students = len(students_df)

total_predictions = len(progress_df)

low_count = len(
    progress_df[
        progress_df["engagement_level"]
        == "Low Engagement"
    ]
)

medium_count = len(
    progress_df[
        progress_df["engagement_level"]
        == "Medium Engagement"
    ]
)

high_count = len(
    progress_df[
        progress_df["engagement_level"]
        == "High Engagement"
    ]
)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Students", total_students)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Predictions", total_predictions)
    st.markdown("</div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Low", low_count)
    st.markdown("</div>", unsafe_allow_html=True)

with c4:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("Medium", medium_count)
    st.markdown("</div>", unsafe_allow_html=True)

with c5:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("High", high_count)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# CHART
# =========================================================

st.markdown("<div class='section-card'>", unsafe_allow_html=True)

st.subheader("📊 Engagement Analytics")

fig = px.histogram(

    progress_df,

    x="engagement_level",

    color="engagement_level",

    title="Student Engagement Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# SEARCH STUDENT
# =========================================================

st.markdown("<div class='section-card'>", unsafe_allow_html=True)

st.subheader("🔍 Search Student")

search_name = st.text_input(
    "Enter Student Name"
)

if search_name:

    filtered_df = progress_df[

        progress_df["student_name"]

        .astype(str)

        .str.contains(

            search_name,

            case=False,

            na=False
        )
    ]

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# LOW ENGAGEMENT
# =========================================================

st.markdown("<div class='section-card'>", unsafe_allow_html=True)

st.subheader("⚠️ Low Engagement Students")

low_students = progress_df[
    progress_df["engagement_level"]
    == "Low Engagement"
]

st.dataframe(
    low_students,
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# STUDENT RECORDS
# =========================================================

st.markdown("<div class='section-card'>", unsafe_allow_html=True)

st.subheader("🎓 Academic Records")

st.dataframe(
    students_df,
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# AI PREDICTIONS
# =========================================================

st.markdown("<div class='section-card'>", unsafe_allow_html=True)

st.subheader("🤖 AI Predictions")

st.dataframe(
    progress_df,
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# LOGOUT
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Logout"):

    st.session_state.logged_in = False
    st.session_state.admin = False

    st.switch_page("frontend.py")

