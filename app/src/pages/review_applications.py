import streamlit as st
from modules.nav import SideBarLinks
SideBarLinks(show_home=True)
# Set page configuration
st.set_page_config(layout="wide")

# Title for the page
st.title("Review Job Applications")

# Description or instructions
st.write("""
    Here you can review job applications submitted by candidates for your job postings.
""")

# Example placeholder for a list of applications
applications = [
    {"Name": "John Doe", "Position": "Software Engineer", "Status": "Pending"},
    {"Name": "Jane Smith", "Position": "Data Analyst", "Status": "Shortlisted"},
]

# Display applications
if applications:
    for application in applications:
        st.write(f"**Name:** {application['Name']}")
        st.write(f"**Position Applied:** {application['Position']}")
        st.write(f"**Status:** {application['Status']}")
        st.write("---")
else:
    st.write("No applications to review at the moment.")
