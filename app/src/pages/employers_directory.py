import streamlit as st
from modules.nav import SideBarLinks
# Page configuration
st.set_page_config(layout="wide")
SideBarLinks(show_home=True)

# Title for the page
st.title("Employers Directory")

# Description
st.write("""
    Use this page to update/delete employers listings.
""")



