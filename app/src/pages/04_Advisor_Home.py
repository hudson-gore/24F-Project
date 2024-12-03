import logging
import streamlit as st

# Set up logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Streamlit page configuration
st.set_page_config(layout="wide")

# Ensure the user is authenticated before accessing the page
if not st.session_state.get('authenticated', False):
    st.error("Please log in to access this page.")
    st.stop()

# Get advisor information from the session state
advisor_name = st.session_state.get('first_name', 'Advisor')

# Page title and description
st.title(f"Welcome, {advisor_name}!")
st.subheader("Your Dashboard for Student Guidance and Career Insights")
st.write("""
    As an advisor, you can use this platform to:
    - Guide students in finding relevant co-op and full-time opportunities.
    - Monitor job placement statistics for your department.
    - Share resources and provide feedback on student profiles.
""")

# Actionable buttons for navigation
if st.button("View Student Profiles"):
    st.write("Navigating to Student Profiles Page... (Not yet implemented)")
if st.button("Job Placement Statistics"):
    st.write("Navigating to Job Placement Statistics Page... (Not yet implemented)")
if st.button("Share Resources"):
    st.write("Navigating to Resources Page... (Not yet implemented)")
if st.button("Provide Feedback"):
    st.write("Navigating to Feedback Page... (Not yet implemented)")
