import streamlit as st
import requests

st.set_page_config(
    page_title = "AI School Management System",
    layout = "centered"
    )

#---------Home Page---------

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "GO To",
    ["Home", "Signup", "Login"]
    )

#--------Home----------

if page == "Home":
    st.title("Ai School Management System")
    
    st.subheader("Smart Student Sanalysis Platform")
    
    st.write(
        "use the sidebar to Signup or Login."
        )
    
    
#-------Signup-------

elif page == "Signup":
    
    st.title("Student Signup")
    
    name = st.text_input("Enter Name")
    
    email = st.text_input("Enter Email")
    
    password = st.text_input("Enter Password", type = "password")
    
    if st.button("Signup"):
        
        signup_data = {
            "name": name,
            "email": email,
            "password": password
            }
        
        response = requests.post(
            "http://127.0.0.1:8000/users",
            
            json = signup_data
            
        )
        
        if response.status_code == 200:
            
            st.success("Signup Sccessfull! Now Login")
            
#---------Login-------

elif page == "Login":
    
    st.title("Student Login")
    
    email = st.text_input("Enter Email")
    
    password = st.text_input("Enter Password", type = "password")
    
    if st.button("Login"):
        
        login_data = {
            "email": email,
            "password": password
            }
        
        response = requests.post(
            "http://127.0.0.1:8000/login",
            
            json = login_data
            )
        
        if response.status_code == 200:
            
            st.success("Login Successfull")
            
            st.subheader("Testing Dashboard")
            
            student_name = st.text_input(
                "Student Name"
                )
            student_class = st.text_input(
                "Maths Marks"
                )
            
            maths_marks = st.number_input(
                "Maths Marks"
                )
            
            science_marks = st.number_input(
                "Science Marks"
                )
            
            st.button("submit")
            
        else:
            st.error(
                "No User found. please Signup first.")