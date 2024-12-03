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
# Get student information from the session state
student_role = st.session_state.get('role', '')
student_name = st.session_state.get('first_name', '')

# Define content based on the persona
if student_role == "jordan_thompson":
    st.title(f"Welcome, {student_name}!")
    st.subheader("Your Journey to Big Tech Starts Here")
    st.write("""
    As an undergraduate computer science student looking to break into the tech industry, 
    you can use this platform to:
    - Find alumni and current students who interned/co-oped at big tech companies.
    - Tailor your profile to impress potential employers.
    - Learn more about contacts to craft personalized emails for networking.
    """)

    # Display actionable buttons or links
    if st.button("Search for Alumni in Big Tech"):
        st.switch_page = "pages/alumni_search.py"
        st.experimental_rerun()

    if st.button("Find Students Who Co-oped at Toast"):
        st.switch_page("pages/co_op_search.py")
        st.experimental_rerun()

    if st.button("Update Your Profile"):
        st.switch_page("pages/profile_update.py")
        st.experimental_rerun()

elif student_role == "maya_chen":
    st.title(f"Welcome, {student_name}!")
    st.subheader("Your Career in Accounting and Finance Awaits")
    st.write("""
    As a senior studying Accounting and Finance, you can use this platform to:
    - Find alumni who made decisions between Accounting and Finance.
    - Aggregate hiring manager information for positions in your fields of interest.
    - Track where others with similar co-op experiences ended up post-graduation.
    """)

    # Display actionable buttons or links
    if st.button("Find Alumni in Accounting and Finance"):
        st.switch_page("pages/alumni_search.py")
        st.experimental_rerun()

    if st.button("Search for Hiring Managers"):
        st.switch_page = "pages/hiring_manager_search.py"
        st.experimental_rerun()

    if st.button("Track Co-op Outcomes"):
        st.switch_page("pages/co_op_outcomes,.py")
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