import streamlit as st
import pandas as pd
import requests

# Function to fetch internships with parameters
def fetch_all_internships(internship_type, locations, companies):
    api_url = "http://api:4000/con/contacts/internships"  # Replace with your actual API base URL
    params = {
        "type": internship_type,  # Send the type parameter (e.g., "current" or "past")
        "locations": ",".join(locations),  # Convert list to comma-separated string
        "companies": ",".join(companies),  # Convert list to comma-separated string
    }
    try:
        # Send GET request with parameters
        response = requests.get(api_url, params=params)
        
        # Debugging: Print the request URL and response
        st.write("API Request URL:", response.url)
        st.write("Raw API Response:", response.json())
        
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):  # Ensure the response is a list of records
                return pd.DataFrame(data)
            else:
                st.error("Unexpected API response format. Expected a list of records.")
                return pd.DataFrame()  # Return an empty DataFrame
        else:
            st.error(f"Error: Received status code {response.status_code}")
            return pd.DataFrame()  # Return an empty DataFrame
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return pd.DataFrame()  # Return an empty DataFrame

# Sidebar Filters
st.sidebar.title("Filters")

# Filter for internship status (current or past)
status = st.sidebar.radio("Internship Status:", ["current", "past"], index=0)

# Filter for internship location
locations = st.sidebar.multiselect(
    "Locations:", ["Boston", "New York", "Chicago"], default=[]
)

# Filter for company
companies = st.sidebar.multiselect(
    "Companies:", ["Google", "Amazon", "Meta", "Oracle"], default=[]
)

# Fetch all internships
st.title("Filtered Internship Data")
if status and (locations or companies):  # Ensure at least one filter is selected
    df = fetch_all_internships(status, locations, companies)
    if not df.empty:
        st.dataframe(df)  # Display the filtered data
    else:
        st.write("No results found for the selected filters.")
else:
    st.write("Please select at least one filter.")
