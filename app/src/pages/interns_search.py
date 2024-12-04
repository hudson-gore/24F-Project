import streamlit as st
import pandas as pd
import requests  # To make API requests
from modules.nav import SideBarLinks  # Import your custom module

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Filters Sidebar", page_icon="⚙️", layout="wide")

# Add navigation links (custom function from your module)
SideBarLinks(show_home=True)

# Sidebar Navigation
st.sidebar.title("Filters")

# Internships Filter
st.sidebar.subheader("Internships")
internship_selection = st.sidebar.radio(
    "Status:",
    options=["current", "past"],
    index=0,
    label_visibility="collapsed"
)

# Location Filter
st.sidebar.subheader("Location")
locations = ["Boston", "New York", "Chicago"]
selected_locations = st.sidebar.multiselect(
    label="",
    options=locations,
    default=["Boston"],  # Default selection
)

# Company Filter
st.sidebar.subheader("Company")
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

# Fetch data from API
if internship_selection and selected_locations and selected_companies:
    try:
        # Build the API request URL and query parameters
        base_url = "http://api:4000/con/contacts/companies/advsisors/students/"  # Replace with your API base URL
        params = {
            "status": internship_selection,
            "location[]": ",".join(selected_locations),
            "CompanyName[]": ",".join(selected_companies),
        }
        
        # Send GET request to the API
        response = requests.get(base_url, params=params)
        
        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            
            # Convert to DataFrame if the data is in list format
            if isinstance(data, list):
                df = pd.DataFrame(data)
                if not df.empty:
                    st.dataframe(df)  # Display the data in a table
                else:
                    st.write("No results found for the selected filters.")
            else:
                st.write("Unexpected response format from API.")
        else:
            st.write(f"Error: Received status code {response.status_code} from the API.")
    except requests.exceptions.RequestException as e:
        st.write(f"API error: {e}")
else:
    st.write("Please select all filters.")
