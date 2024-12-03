import streamlit as st
from modules.nav import SideBarLinks
SideBarLinks(show_home=True)
# Page configuration
st.set_page_config(layout="wide")

# Title for the page
st.title("Provide Feedback")

# Description
st.write("""
    Use this page to provide feedback on student profiles, resumes, or applications.
""")

# Input field for student name or ID
student_id = st.text_input("Enter Student Name or ID:")

# Text area for feedback
feedback = st.text_area("Enter your feedback:")

# Button to submit feedback
if st.button("Submit Feedback"):
    if student_id and feedback:
        st.success(f"Feedback submitted for {student_id}!")
        st.write("This feature is under construction.")
    else:
        st.error("Please provide both a student name/ID and feedback.")
