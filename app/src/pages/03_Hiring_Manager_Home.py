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

# Get hiring manager information from the session state
hiring_manager_name = st.session_state.get('first_name', '')
hiring_manager_role = st.session_state.get('role', '')

# Display the hiring manager home page content
if hiring_manager_role == "hiring_manager":
    st.title(f"Welcome, {hiring_manager_name}!")
    st.subheader("Your Platform for Hiring and Talent Management")
    st.write("""
    As a hiring manager, you can use this platform to:
    - Post new job openings.
    - Review applications and candidate profiles.
    - Search for potential candidates based on skills and experience.
    - Track the status of your job listings and applications.
    """)

    # Actionable buttons for navigation
    if st.button("Post a New Job Opening"):
        st.session_state.page = "post_job"
        st.experimental_rerun()

    if st.button("Review Job Applications"):
        st.session_state.page = "review_applications"
        st.experimental_rerun()

    if st.button("Search for Candidates"):
        st.session_state.page = "search_candidates"
        st.experimental_rerun()

    if st.button("Track Job Listing Status"):
        st.session_state.page = "job_listing_status"
        st.experimental_rerun()

else:
    st.error("Unknown hiring manager role. Please log in again.")
    logger.error(f"Unknown hiring manager role: {hiring_manager_role}")

# Import pages based on session state for navigation
if 'page' in st.session_state:
    page = st.session_state.page
else:
    page = None

if page == "post_job":
    import post_job
elif page == "review_applications":
    import review_applications
elif page == "search_candidates":
    import search_candidates
elif page == "job_listing_status":
    import job_listing_status
else:
    st.write("Hiring Manager Home Page (Default)")
