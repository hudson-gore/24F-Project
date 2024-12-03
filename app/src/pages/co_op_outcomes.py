import streamlit as st
from modules.nav import SideBarLinks
SideBarLinks(show_home=True)
# Set page config for Streamlit
st.set_page_config(layout="wide")

# Title of the page
st.title("Track Co-op Outcomes")

# Add description or instructions
st.write("""
    Here you can track where students who have completed similar co-ops ended up post-graduation.
""")

# Example input for co-op experience search
co_op_experience = st.text_input("Enter your co-op experience (e.g., Data Science, Accounting):")

if co_op_experience:
    st.write(f"Tracking co-op outcomes for students with {co_op_experience} experience...")
    # Placeholder for actual search logic
    st.write("This feature is under construction.")
