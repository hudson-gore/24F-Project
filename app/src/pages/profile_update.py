import streamlit as st
from modules.nav import SideBarLinks
# Set page config for Streamlit
st.set_page_config(layout="wide")
SideBarLinks(show_home=True)

# Title of the page
st.title("Update Your Profile")

# Add description or instructions
st.write("""
    Here you can update your profile information, such as contact details, resume, and other personal information.
""")

# Example fields for updating profile
name = st.text_input("Enter your name:")
email = st.text_input("Enter your email:")
location = st.text_input("Enter your location:")
bio = st.text_input("Enter your bio:")

if st.button("Save Profile"):
    st.write("Saving your profile information...")
    # Placeholder for actual profile update logic
    st.write("This feature is under construction.")
