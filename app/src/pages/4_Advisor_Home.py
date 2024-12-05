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

# Get advisor information from the session state
advisor_name = st.session_state.get('first_name', '')

# Display the title and welcome message
st.title(f"Welcome, {advisor_name}!")
st.text("Dr. Sarah Patel is a co-op advisor at Northeastern University dedicated to guiding students \
        on the journey to finding their first, second, or third co-op. She is in charge of overseeing \
        all of the resources available to students for networking with employers, other students, or alumni.")
st.subheader(" ")

# Navigation buttons
if st.button("Delete Severed Relationships", type='primary', use_container_width=True):
    st.switch_page("pages/4_1_delete_company.py")

if st.button("Student Application Dashboard", type='primary', use_container_width=True):
    st.switch_page("pages/4_2_application_dashboard.py")

if st.button("Add a Tag to A Student", type='primary', use_container_width=True):
    st.switch_page("pages/4_3_tagging_students.py")

if st.button("Add a New Contact to Database", type='primary', use_container_width=True):
    st.switch_page("pages/4_4_adding_new_contacts.py")