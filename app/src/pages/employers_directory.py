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

# Example input to search Employers
industry = st.text_input("Enter an Industry Name:")
tag = st.text_input("Comapny Name:")

with st.expander("Role Type"):
    roles = st.multiselect(
        "Select Job Listings Looking For", ["Software Engineer", "Data Analyst", "Cloud Engineer", "QRole", "IT"], default=["Software Engineer"]
    )
    st.write(f"Selected {len(roles)}/5")


