import streamlit as st
import requests

st.set_page_config(page_title="Student Portal")
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# TABS
login_tab, signup_tab = st.tabs(["Login", "Signup"])

# ---------------- LOGIN ---------------- #

with login_tab:

    st.title("Student Login Portal")

    email = st.text_input("Login Email")
    password = st.text_input("Login Password", type="password")

    if st.button("Login"):

        login_data = {
            "email": email,
            "password": password
        }

        response = requests.post(
            "http://127.0.0.1:8000/login",
            json=login_data
        )

        if response.status_code == 200:

            st.session_state.logged_in = True

            st.success("Login Successful")

            st.switch_page("pages/dashboard.py")

        else:
            st.error("Invalid Credentials")


# ---------------- SIGNUP ---------------- #

with signup_tab:

    st.title("Student Signup")

    name = st.text_input("Enter Name")

    signup_email = st.text_input("Enter Signup Email")

    signup_password = st.text_input(
        "Enter Signup Password",
        type="password"
    )

    if st.button("Signup"):

        signup_data = {
            "name": name,
            "email": signup_email,
            "password": signup_password
        }

        response = requests.post(
            "http://127.0.0.1:8000/users",
            json=signup_data
        )

        if response.status_code == 200:

            st.success("Signup Successful! Now Login")

        else:

            st.error(response.text)