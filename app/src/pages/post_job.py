import streamlit as st

# Set page configuration
st.set_page_config(layout="wide")

# Title for the page
st.title("Post a New Job Opening")

# Description or instructions
st.write("""
    Use this page to post a new job opening. Provide the necessary details, 
    and the listing will be added to the platform for potential candidates to view.
""")

# Input fields for job details
job_title = st.text_input("Job Title:")
job_description = st.text_area("Job Description:")
skills_required = st.text_input("Required Skills (comma-separated):")
location = st.text_input("Location:")
salary = st.text_input("Salary Range (optional):")

# Submit button
if st.button("Submit Job Posting"):
    # Placeholder for saving the job posting logic
    st.success("Your job posting has been submitted!")
    st.write(f"### Job Title: {job_title}")
    st.write(f"**Description:** {job_description}")
    st.write(f"**Skills Required:** {skills_required}")
    st.write(f"**Location:** {location}")
    st.write(f"**Salary:** {salary if salary else 'Not specified'}")
