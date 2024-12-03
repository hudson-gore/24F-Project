# import logging
# import streamlit as st
# from modules.nav import SideBarLinks
# # Set up logging
# logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Streamlit page configuration
# st.set_page_config(layout="wide")
# SideBarLinks(show_home=True)
# # Ensure the user is authenticated before accessing the page
# if not st.session_state.get('authenticated', False):
#     st.error("Please log in to access this page.")
#     st.stop()

# # Get hiring manager information from the session state
# hiring_manager_name = st.session_state.get('first_name', '')
# hiring_manager_role = st.session_state.get('role', '')

# # Display the hiring manager home page content
# if hiring_manager_role == "hiring_manager":
#     st.title(f"Welcome, {hiring_manager_name}!")
#     st.subheader("Your Platform for Hiring and Talent Management")
#     st.write("""
#     As a hiring manager, you can use this platform to:
#     - Post new job openings.
#     - Review applications and candidate profiles.
#     - Search for potential candidates based on skills and experience.
#     - Track the status of your job listings and applications.
#     """)

#     # Actionable buttons for navigation
#     if st.button("Post a New Job Opening"):
#         st.switch_page("pages/post_job.py")

#     if st.button("Review Job Applications"):
#         st.switch_page("pages/review_applications.py")
#         st.experimental_rerun()

#     if st.button("Search for Candidates"):
#         st.switch_page("pages/search_candidates.py")
#         st.experimental_rerun()

#     if st.button("Track Job Listing Status"):
#         st.switch_page("pages/job_listing_status.py")
#         st.experimental_rerun()

# else:
#     st.error("Unknown hiring manager role. Please log in again.")
#     logger.error(f"Unknown hiring manager role: {hiring_manager_role}")

# # Import pages based on session state for navigation
# if 'page' in st.session_state:
#     page = st.session_state.page
# else:
#     page = None

# if page == "post_job":
#     import post_job
# elif page == "review_applications":
#     import review_applications
# elif page == "search_candidates":
#     import search_candidates
# elif page == "job_listing_status":
#     import job_listing_status
# else:
#     st.write("Hiring Manager Home Page (Default)")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
# Simulated data
months = ['August', 'September', 'October', 'November', 'December']
engagement_data = [50, 150, 250, 200, 100]

academic_years = ['1st Year', '2nd Year', '3rd Year', '4th Year', '5th Year']
academic_year_counts = [50, 40, 80, 60, 30]

majors = ['Data Science', 'Information Systems', 'Mathematics', 'Computer Science']
major_counts = [80, 60, 40, 100]

recent_interactions = [
    ('Sarah Patel', 'patel.s@northeastern.edu'),
    ('maya Chen', 'maya.l@northeastern.edu'),
    ('Jordan Thompson', 'jordan.n@northeastern.edu'),
    ('Mia Patel', 'patel.m@northeastern.edu')
]

# Set up the Streamlit page
st.set_page_config(layout="wide")

hiring_manager_name = st.session_state.get('first_name', '')
hiring_manager_role = st.session_state.get('role', '')

# Dashboard Header
st.title('Dashboard')
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
st.subheader('Alex Rivera')

# Total Engagement Section
st.markdown('### Total Engagement')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(months, engagement_data, marker='o', color='b')
ax.set_title('Total Engagement')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Interactions')
st.pyplot(fig)

# Academic Year Distribution
st.markdown('### Academic Year')
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(academic_year_counts, labels=academic_years, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(academic_years)))
ax.set_title('Academic Year Distribution')
st.pyplot(fig)

# Major Distribution
st.markdown('### Major Distribution')
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(major_counts, labels=majors, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2", len(majors)))
ax.set_title('Major Distribution')
st.pyplot(fig)

# Recent Interactions
st.markdown('### Recent Interactions')
interaction_data = pd.DataFrame(recent_interactions, columns=['Tag', 'Student Name', 'Email'])
st.dataframe(interaction_data)

# Layout customization for the sidebar and main content
with st.sidebar:
    st.markdown('### Dashboard Views')
    st.radio("Select View", ('Contacts', 'Total Views', 'Total Engagement', 'Major Distribution', 'Academic Year', 'GPA Distribution', 'Recent Interactions'))

# Actionable buttons for navigation
st.markdown('---')  # Add a line separator before the buttons

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Post a New Job Opening"):
        st.switch_page("pages/post_job.py")

with col2:
    if st.button("Review Job Applications"):
        st.switch_page("pages/review_applications.py")
        st.experimental_rerun()

with col3:
    if st.button("Search for Candidates"):
        st.switch_page("pages/search_candidates.py")
        st.experimental_rerun()

with col4:
    if st.button("Track Job Listing Status"):
        st.switch_page("pages/job_listing_status.py")
        st.experimental_rerun()

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