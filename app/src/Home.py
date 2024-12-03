import logging
import streamlit as st
from modules.nav import SideBarLinks

# Set up logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Set page layout
st.set_page_config(layout='wide')

# Session state to handle user authentication
st.session_state['authenticated'] = False

# Use the SideBarLinks function from modules/nav.py for navigation
SideBarLinks(show_home=True)

# Content for the home page
logger.info("Loading the Home page of the app")
st.title('NetWorkHub')
st.write('\n\n')
st.write('Welcome to NetWorkHub! Please select a user persona to proceed:')

# Persona buttons
if st.button("Jordan Thompson", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'jordan_thompson'
    st.session_state['first_name'] = 'Jordan'
    logger.info("Logging in as Jordan Thompson")
    st.switch_page('pages/01_Student_Home.py') 

if st.button("Maya Chen", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'student'
    st.session_state['first_name'] = 'Maya'
    logger.info("Logging in as Maya Chen")
    st.switch_page('pages/02_Student_Home.py')  

if st.button("Alex Rivera", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'hiring_manager'
    st.session_state['first_name'] = 'Alex'
    logger.info("Logging in as Alex Rivera")
    st.switch_page('pages/03_Hiring_Manager_Home.py')  

if st.button("Dr. Sarah Patel", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'co_op_advisor'
    st.session_state['first_name'] = 'Sarah'
    logger.info("Logging in as Dr. Sarah Patel")
    st.switch_page('pages/04_Advisor_Home.py')
