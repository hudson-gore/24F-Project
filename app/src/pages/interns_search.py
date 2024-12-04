import streamlit as st

# Set page configuration
st.set_page_config(page_title="Filters Sidebar", page_icon="⚙️", layout="wide")

# Add sidebar for filters
st.sidebar.title("Filters")

# Co-ops Filter
st.sidebar.subheader("Internships")
internship_selection = st.sidebar.radio(
    "Status:",
    options=["current", "past"],
    index=0,
    label_visibility="collapsed"
)

# Location Filter
st.sidebar.subheader("location")
locations = ["Boston", "New York", "Chicago"]
selected_locations = st.sidebar.multiselect(
    label="",
    options=locations,
    default=["Boston"],  # Default selection
)

# Company Filter
st.sidebar.subheader("company")
companies = ["Google", "Amazon", "Meta", "Oracle"]
selected_companies = st.sidebar.multiselect(
    label="",
    options=companies,
    default=["Google", "Amazon"],  # Default selection
)

# Display selected filters
st.write("### Selected Filters:")
st.write(f"**Internship Status:** {internship_selection}")
st.write(f"**Locations:** {', '.join(selected_locations) if selected_locations else 'None'}")
st.write(f"**Companies:** {', '.join(selected_companies) if selected_companies else 'None'}")


if st.sidebar.button("Menu"):
    st.switch_page("pages/student_home.py")

