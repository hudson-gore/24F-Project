##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports regular and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout='wide')

# If a user is at this page, we assume they are not 
# authenticated. So we change the 'authenticated' value
# in the streamlit session_state to false.
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('NetWorkHub')
st.write('\n\n')
st.write('Welcome to NetWorkHub! Please select a user persona to proceed:')

# Persona buttons

#Jordans button
if st.button("Jordan Thompson", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'student'
    st.session_state['first_name'] = 'Jordan'
    logger.info("Logging in as Jordan Thompson")
    st.switch_page('pages/01_Student_Home.py')
# Maya chen button
if st.button("Maya Chen", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'student'
    st.session_state['first_name'] = 'Maya'
    logger.info("Logging in as Maya Chen")
    st.switch_page('pages/02_Student_Home.py')

## Alex Riveras button
if st.button("Alex Rivera", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'hiring_manager'
    st.session_state['first_name'] = 'Alex'
    logger.info("Logging in as Alex Rivera")
    st.switch_page('pages/03_Hiring_Manager_Home.py')


## Sarah patel's button
if st.button("Dr. Sarah Patel", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'co_op_advisor'
    st.session_state['first_name'] = 'Sarah'
    logger.info("Logging in as Dr. Sarah Patel")
    st.switch_page('pages/04_Advisor_Home.py')
