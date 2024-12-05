import logging
import streamlit as st
from modules.nav import SideBarLinks
import random

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


# Get hiring manager information from the session state
hiring_manager_name = st.session_state.get('first_name', '')
hiring_manager_role = st.session_state.get('role', '')

# Display the hiring manager home page content
if hiring_manager_role == "hiring_manager":
    st.title(f"Welcome, {hiring_manager_name}!")
    st.text('Alex Rivera is a Northeastern Graduate, who now is the hiring manager for Wayfair. \
            Alex is in charge of overseeing all of the co-op hiring processes within Wayfair and \
            maintaining the relationship between Northeastern and Wayfair.')
    st.subheader(' ')

    # Actionable buttons for navigation
    if st.button("Current students who have interned at big tech firms as Software Engineers", type='primary', use_container_width=True):
        st.switch_page("pages/post_job.py")

    if st.button("Current students who have interned at big tech firms as Software Engineers", type='primary', use_container_width=True):
        st.switch_page("pages/review_applications.py")
        st.experimental_rerun()

    if st.button("Current students who have interned at big tech firms as Software Engineers", type='primary', use_container_width=True):
        st.switch_page("pages/search_candidates.py")
        st.experimental_rerun()

    if st.button("Current students who have interned at big tech firms as Software Engineers", type='primary', use_container_width=True):
        st.switch_page("pages/job_listing_status.py")
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