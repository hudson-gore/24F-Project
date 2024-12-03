import streamlit as st
from modules.nav import SideBarLinks
import requests

# Page configuration
st.set_page_config(layout="centered")
SideBarLinks(show_home=True)

# Title and subheader for the page
st.title("Student Directory")
st.subheader("Use this page to search and view profiles of students seeking co-op and full-time opportunities.")


# Example input to search hiring managers
company_name = st.text_input("Enter a company name (e.g., Deloitte, EY):")

if company_name:
    st.write(f"Searching for hiring managers at {company_name}...")
    # Placeholder for actual search logic
    st.write("This feature is under construction.")
