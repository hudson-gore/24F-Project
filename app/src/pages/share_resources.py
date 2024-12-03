import streamlit as st
from modules.nav import SideBarLinks
SideBarLinks(show_home=True)
# Page configuration
st.set_page_config(layout="wide")

# Title for the page
st.title("Share Resources")

# Description
st.write("""
    Use this page to share helpful resources with students, such as job boards, articles, or templates.
""")

# Input fields to add resources
resource_title = st.text_input("Resource Title:")
resource_link = st.text_input("Resource Link (URL):")
resource_description = st.text_area("Resource Description:")

# Button to share the resource
if st.button("Share Resource"):
    if resource_title and resource_link:
        st.success(f"Resource '{resource_title}' shared successfully!")
        st.write("This feature is under construction.")
    else:
        st.error("Please provide both a title and a link for the resource.")
