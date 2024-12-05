import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

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
# Get student information from the session state
student_role = st.session_state.get('role', '')
student_name = st.session_state.get('first_name', '')


# Define content based on the persona
if student_role == "jordan_thompson":
    st.title(f"Welcome, {student_name}!")
    st.text('Jordan Thompson is an undergraduate student at Northeastern University majoring in computer science, \
            with a minor in applied mathematics. Jordan is currently in the second year of his degree and has begun \
            searching for a co-op for the upcoming spring semester. He is most interested in being a software \
            developer for one of the larger tech companies (Google, Amazon, Apple. Meta, Microsoft, etc.), but is \
            open to other opportunities in the start-up space as well.')
    st.subheader(" ")

    # Display actionable buttons with hover animation
    if st.button("Current students who have interned at big tech firms as Software Engineers", type='primary', use_container_width=True):
        st.switch_page("pages/1_1_intern_search.py")
        st.experimental_rerun()

    if st.button("Alumni who work in Tech", type='primary', use_container_width=True):
        st.switch_page("pages/1_2_alumni_industry.py")
        st.experimental_rerun()

    if st.button("Looking for a specific employer's profile", type='primary', use_container_width=True):
        st.switch_page("pages/1_3_specific_profile.py")
        st.experimental_rerun()

    if st.button("Student's who have done Software Development at Toast", type='primary', use_container_width=True):
        st.switch_page("pages/1_4_students_internships.py")
        st.experimental_rerun()

elif student_role == "maya_chen":
    st.title(f"Welcome, {student_name}!")
    st.text("Maya Chen is an undergraduate student at Northeastern University studying \
            Accounting and Finance. Maya is in their first semester of her senior year \
            and thus far has successfully completed a co-op in Audit at PWC and as a \
            Financial Analyst for Fidelity. As her time at Northeastern comes to a close \
            she is looking for a full-time position, but is unsure if she wants to stay \
            in Finance or go back to Accounting. ")
    st.subheader(" ")
    

    # Display actionable buttons with hover animation
    if st.button("Find alumni who graduated with an Accounting and Finance Degree", type='primary', use_container_width=True):
        st.switch_page("pages/2_1_alumni_search.py")
        st.experimental_rerun()

    if st.button("Adjust my profile to indicated I am looking for a job", type='primary', use_container_width=True):
        st.switch_page("pages/2_2_profile_update.py")
        st.experimental_rerun()

    if st.button("Aggregate a list of hiring managers in Accounting and Finance", type='primary', use_container_width=True):
        st.switch_page("pages/2_3_hiring_managers.py")
        st.experimental_rerun()

    if st.button("Add my co-op experiences to the data-base", type='primary', use_container_width=True):
        st.switch_page("pages/2_4_add_internship.py")
        st.experimental_rerun()

else:
    st.error("Unknown student role. Please log in again.")
    logger.error(f"Unknown student role: {student_role}")

# Import pages based on session state for navigation
if 'page' in st.session_state:
    page = st.session_state.page
else:
    page = None

if page == "alumni_search":
    import alumni_search
elif page == "co_op_search":
    import co_op_search
elif page == "profile_update":
    import profile_update
elif page == "hiring_manager_search":
    import hiring_managers
elif page == "co_op_outcomes":
    import co_op_outcomes