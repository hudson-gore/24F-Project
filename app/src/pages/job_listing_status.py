import streamlit as st
from modules.nav import SideBarLinks
# Set page configuration
st.set_page_config(layout="wide")
SideBarLinks(show_home=True)

# Title for the page
st.title("Track Job Listing Status")

# Description or instructions
st.write("""
    Use this page to track the status of your job listings, including views, applications received, 
    and hiring progress.
""")

# Example placeholder for job listing statuses
job_listings = [
    {"Title": "Software Engineer", "Views": 120, "Applications": 10, "Status": "Open"},
    {"Title": "Data Scientist", "Views": 95, "Applications": 5, "Status": "Closed"},
]

# Display job listing statuses
if job_listings:
    for listing in job_listings:
        st.write(f"**Job Title:** {listing['Title']}")
        st.write(f"**Views:** {listing['Views']}")
        st.write(f"**Applications:** {listing['Applications']}")
        st.write(f"**Status:** {listing['Status']}")
        st.write("---")
else:
    st.write("No job listings found.")
