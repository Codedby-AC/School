import streamlit as st
import requests
st.set_page_config(page_title="Dashboard")

st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# SECURITY CHECK
if "logged_in" not in st.session_state:
    st.switch_page("frontend.py")

st.title("Student Dashboard")

st.success("Welcome To Dashboard")
#--------Dashboard---------

if "logged_in" not in st.session_state:
    st.warning("Please login first")
    st.stop()

if st.session_state.logged_in:

    st.title("🎓 Student Academic Portal")

    st.success("AI Powered Academic Dashboard")

    # =========================
    # PAGE SELECTOR
    # =========================

    page = st.radio(
        "Choose Section",
        [
            "Student Registration",
            "Engagement Predictor"
        ]
    )

    # =====================================================
    # STUDENT REGISTRATION PAGE
    # =====================================================

    if page == "Student Registration":

        st.subheader("📚 Student Registration Form")

        name = st.text_input("Student Name")

        student_class = st.text_input("Class")

        section = st.text_input("Section")

        roll_number = st.number_input(
            "Roll Number",
            min_value=1
        )

        maths_marks = st.number_input(
            "Maths Marks",
            min_value=0,
            max_value=100
        )

        science_marks = st.number_input(
            "Science Marks",
            min_value=0,
            max_value=100
        )

        english_marks = st.number_input(
            "English Marks",
            min_value=0,
            max_value=100
        )

        if st.button("Save Academic Details"):

            student_data = {
                "name": name,
                "student_class": student_class,
                "section": section,
                "roll_number": int(roll_number),
                "maths_marks": maths_marks,
                "science_marks": science_marks,
                "english_marks": english_marks
            }

            response = requests.post(
                "http://127.0.0.1:8000/students",
                json=student_data
            )

            if response.status_code == 200:

                st.success(
                    "✅ Student Registered Successfully"
                )

            else:

                st.error(response.text)

    # =====================================================
    # ENGAGEMENT PREDICTOR PAGE
    # =====================================================

    elif page == "Engagement Predictor":

        st.subheader("🤖 Student Engagement Predictor")

        student_name = st.text_input(
            "Student Name"
        )

        raisedhands = st.slider(
            "Raised Hands",
            0,
            100
        )

        visited_resources = st.slider(
            "Visited Resources",
            0,
            100
        )

        announcements = st.slider(
            "Announcements View",
            0,
            100
        )

        discussion = st.slider(
            "Discussion",
            0,
            100
        )

        if st.button("Predict Engagement"):

            engagement_data = {

                "student_name": student_name,

                "raisedhands": raisedhands,

                "visited_resources": visited_resources,

                "announcements": announcements,

                "discussion": discussion
            }

            response = requests.post(
                "http://127.0.0.1:8000/predict_engagement",
                json=engagement_data
            )

            if response.status_code == 200:

                result = response.json()

                st.success(
                    f"🎯 Engagement Level: {result['engagement_level']}"
                )

            else:

                st.error(response.text)