import streamlit as st
from modules.nav import SideBarLinks
# Set page config for Streamlit
st.set_page_config(layout="wide")
SideBarLinks(show_home=True)
# Title of the page
st.title("Find Students Who Co-oped at Toast")

# Add description or instructions
st.write("""
    Here you can search for students who have completed co-ops at Toast.
""")

# Example input to search students
student_name = st.text_input("Enter student name to search co-op experience:")

if student_name:
    st.write(f"Searching for co-op information for {student_name}...")
    # Placeholder for actual search logic
    st.write("This feature is under construction.")
