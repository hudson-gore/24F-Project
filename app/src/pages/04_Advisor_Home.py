import logging
import streamlit as st
from modules.nav import SideBarLinks
# Set up logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Streamlit page configuration
st.set_page_config(layout="wide")
SideBarLinks(show_home=True)
# Ensure the user is authenticated before accessing the page
if not st.session_state.get('authenticated', False):
    st.error("Please log in to access this page.")
    st.stop()

# Get advisor information from the session state
advisor_name = st.session_state.get('first_name', '')

# Display the title and welcome message
st.title(f"Welcome, {advisor_name}!")
st.subheader("Advisor Home Page")
st.write("""
As an advisor, you can use this platform to:
- View student profiles.
- Analyze job placement statistics.
- Share resources with students.
- Provide feedback on student materials.
""")

seach_query = st.text_input("Search for a student:", "")

# Navigation buttons
if st.button("Student Directory"):
    st.write("Navigating to Student Directory...")
    st.switch_page("pages/student_directory.py")

if st.button("Analyze Job Placement Statistics"):
    st.write("Navigating to Job Placement Statistics...")
    st.switch_page("pages/job_placement_statistics.py")

if st.button("Share Resources"):
    st.write("Navigating to Share Resources...")
    st.switch_page("pages/share_resources.py")


if st.button("Provide Feedback"):
    st.write("Navigating to Provide Feedback...")
    st.switch_page("pages/provide_feedback.py")

if st.button("Employers"):
    st.write("Navigative to Employers...")
    st.switch_page("pages/employers_directory.py")