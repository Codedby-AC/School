import streamlit as st
import requests

if "logged_in" not in st.session_state:
    
    st.session_state.logged_in = False
    
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.set_page_config(
    page_title = "AI School Management System",
    layout = "centered"
    )

#---------Home Page---------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "GO To",
    ["Home", "Signup"]
    )

#--------Home----------

if page == "Home":
    
    st.title("Ai School Management System")
    
    st.subheader("Smart Student Sanalysis Platform")
    
    st.write(
        "Welcome to the AI-Powered School Maanagement System")
    
    st.write(
        "Please login to continue."
        )
    
#Login Form
    
    email = st.text_input("Enter Email")

    password = st.text_input(
        "Enter password",
        type = "password"
    )

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
            
            st.session_state.logged_in = True
            
            st.success("Login Successful")
            
            st.session_state.logged_in = True
            
            st.session_state.page = "Dashboard"
            
            st.rerun()
            
        else:
            
            st.error(
                "Invalid email or password"
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
            

#--------Dashboard---------

if st.session_state.logged_in:
    
    st.title("Student Academic Portal")
    
    st.success("Complete Academic Portal")
    
    st.subheader("Student Registration Form")
    
    name = st.text_input("Student Name")
    
    student_class = st.text_input("Class")
    
    section = st.text_input("Section")
    
    roll_number = st.number_input("Roll Number", min_value = 1)
    
    maths_marks = st.number_input("Maths Marks", min_value=0, max_value=100)
    
    science_marks = st.number_input("Science Marks",min_value = 0, max_value = 100)
    
    english_marks = st.number_input("English Marks", min_value = 0, max_value=100)
    
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
            
            json = student_data
            )
        if response.status_code == 200:
            
            st.success(
                "Student Registeres Successfully"
                )
            
        else:
            st.error(response.text)
        