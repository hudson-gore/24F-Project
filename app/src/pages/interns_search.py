import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Function to fetch all internships from the API
def fetch_all_internships():
    api_url = "http://api:4000/internships/<position>"  # Replace with your actual API base URL
    
    try:
        response = requests.get(api_url)
        st.write("API Request URL:", response.url)
        st.write("Raw API Response:", response.json())  # Debugging output
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
df = fetch_all_internships()

if not df.empty:
    # Ensure StartDate and EndDate columns are in datetime format
    df["StartDate"] = pd.to_datetime(df["StartDate"])
    df["EndDate"] = pd.to_datetime(df["EndDate"])

    # Filter by internship status (current or past)
    today = datetime.now()
    if status == "current":
        df = df[df["StartDate"] <= today]  # Internship has started
        df = df[df["EndDate"] >= today]  # Internship hasn't ended
    elif status == "past":
        df = df[df["EndDate"] < today]  # Internship ended in the past

    # Filter by location
    if locations:
        df = df[df["Location"].isin(locations)]

    # Filter by company
    if companies:
        df = df[df["CompanyName"].isin(companies)]

    # Display the filtered data
    if not df.empty:
        st.write("### Filtered Internship Data")
        st.dataframe(df)  # Display the DataFrame
    else:
        st.write("No results found for the selected filters.")
else:
    st.write("Failed to load internship data. Please check the API or your connection.")
