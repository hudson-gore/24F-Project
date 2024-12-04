import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Function to fetch all internships from the API
def fetch_all_internships():
    api_url = "http://localhost:4000/internships"  # Replace with your actual API base URL
    try:
        response = requests.get(api_url)
        st.write("API Request URL:", response.url)  # Debugging
        if response.status_code == 200:
            data = response.json()
            st.write("Raw API Response:", data)  # Debugging
            if isinstance(data, list):  # Ensure the response is a list of records
                return pd.DataFrame(data)
            else:
                st.error("Unexpected API response format. Expected a list of records.")
                return pd.DataFrame()
        else:
            st.error(f"Error: Received status code {response.status_code}")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return pd.DataFrame()

# Function to fetch internship holders for a specific position
def fetch_internship_holders(position):
    api_url = f"http://localhost:4000/internships/{position}"  # Replace with your actual API base URL
    try:
        response = requests.get(api_url)
        st.write("API Request URL:", response.url)  # Debugging
        if response.status_code == 200:
            data = response.json()
            st.write("Raw API Response:", data)  # Debugging
            if isinstance(data, list):  # Ensure the response is a list of records
                return pd.DataFrame(data)
            else:
                st.error("Unexpected API response format. Expected a list of records.")
                return pd.DataFrame()
        else:
            st.error(f"Error: Received status code {response.status_code}")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return pd.DataFrame()

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

# Input for Position ID (optional)
position_id = st.sidebar.text_input("Position ID (Optional):")

# Fetch data based on filters
st.title("Filtered Internship Data")
if position_id:
    # Fetch specific internship holders
    df = fetch_internship_holders(position_id)
else:
    # Fetch all internships
    df = fetch_all_internships()

if not df.empty:
    # Ensure StartDate and EndDate columns are in datetime format
    if "StartDate" in df.columns:
        df["StartDate"] = pd.to_datetime(df["StartDate"])
    if "EndDate" in df.columns:
        df["EndDate"] = pd.to_datetime(df["EndDate"])

    # Filter by internship status (current or past)
    if "StartDate" in df.columns and "EndDate" in df.columns:
        today = datetime.now()
        if status == "current":
            df = df[(df["StartDate"] <= today) & (df["EndDate"] >= today)]
        elif status == "past":
            df = df[df["EndDate"] < today]

    # Filter by location
    if locations and "Location" in df.columns:
        df = df[df["Location"].isin(locations)]

    # Filter by company
    if companies and "Company" in df.columns:
        df = df[df["Company"].isin(companies)]

    # Display the filtered data
    if not df.empty:
        st.write("### Filtered Internship Data")
        st.dataframe(df)
    else:
        st.write("### Sorry, there is nothing for these selections.")
else:
    st.write("### Sorry, there is nothing for these selections.")
