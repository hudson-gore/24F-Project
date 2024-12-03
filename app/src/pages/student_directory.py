import streamlit as st
from modules.nav import SideBarLinks
# Page configuration
st.set_page_config(layout="wide")
SideBarLinks(show_home=True)

# Title for the page
st.title("Student Directory")

# Description
st.write("""
    Use this page to search and view profiles of students seeking co-op and full-time opportunities.
""")

# Example input field for searching student profiles
student_name = st.text_input("Enter a student name:")

# Placeholder logic for searching profiles
if student_name:
    st.write(f"Searching for student profiles matching: {student_name}")
    st.write("This feature is under construction.")
