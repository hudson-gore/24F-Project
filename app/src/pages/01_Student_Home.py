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
# Get student information from the session state
student_role = st.session_state.get('role', '')
student_name = st.session_state.get('first_name', '')
messages = [
    "Your journey to success starts here!",
    "Unlock your potential, step by step.",
    "Learn, grow, and make an impact.",
    "Curiosity leads to opportunities.",
    "Dream big, work hard, achieve more.",
    "The world is ready for your talents.",
    "Every effort takes you closer to your goals.",
    "Turning ideas into opportunities starts now.",
    "Your career future is full of possibilities.",
    "Break boundaries and build your path.",
    "Charting the way to your dreams.",
    "Design the future you want to see.",
    "Where passion meets purpose.",
    "Every application brings new possibilities."
]

# Define content based on the persona
if student_role == "jordan_thompson":
    st.title(f"hi, {student_name}!")
    st.subheader("Student Homepage")
    message = random.choice(messages)

    # Make it fancy using HTML with animations
    st.markdown(f"""
    <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; 
                text-align: center; font-size: 24px; font-weight: bold; 
                color: #4b0082; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                animation: fadeIn 2s ease-in-out;">
     <span style="color: #11178f;">{message}</span>
    </div>

    <style>
        @keyframes fadeIn {{
            from {{
                opacity: 0;
            }}
            to {{
                opacity: 1;
            }}
        }}
    </style>
    """, unsafe_allow_html=True)

    st.text("\n")

    # Display actionable buttons with hover animation
    if st.button("Coops"):
        st.switch_page("pages/co_op_search.py")
        st.experimental_rerun()

    if st.button("Interns"):
        st.switch_page("pages/interns_search.py")
        st.experimental_rerun()

    if st.button("Alumni"):
        st.switch_page("pages/alumni_search.py")
        st.experimental_rerun()

    if st.button("Update Your Profile"):
        st.switch_page("pages/profile_update.py")
        st.experimental_rerun()

elif student_role == "maya_chen":
    st.title(f"Welcome, {student_name}!")
    st.subheader("Student Homepage")
    
    message = random.choice(messages)
    
    st.markdown(f"""
    <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; 
                text-align: center; font-size: 24px; font-weight: bold; 
                color: #4b0082; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                animation: fadeIn 2s ease-in-out;">
     <span style="color: #11178f;">{message}</span>
    </div>

    <style>
        @keyframes fadeIn {{
            from {{
                opacity: 0;
            }}
            to {{
                opacity: 1;
            }}
        }}
    </style>
    """, unsafe_allow_html=True)
    
    st.text("\n")

    # Display actionable buttons with hover animation
    if st.button("Find Alumni in Accounting and Finance"):
        st.switch_page("pages/alumni_search.py")
        st.experimental_rerun()

    if st.button("Search for Hiring Managers"):
        st.switch_page("pages/hiring_managers.py")
        st.experimental_rerun()

    if st.button("Track Co-op Outcomes"):
        st.switch_page("pages/co_op_outcomes.py")
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
else:
    st.write("Home Page (Default)")