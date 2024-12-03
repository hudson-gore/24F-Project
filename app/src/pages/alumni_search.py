import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Set page config for Streamlit
st.set_page_config(layout="wide")
SideBarLinks(show_home=True)

# Title of the page
st.title("Contact Search")

# Add description or instructions
st.write("""
    Search For All of The Contacts in A Specific Industry With a Specific Tag
""")

# Example input to search contacts
industry = st.text_input("Enter an Industry Name:")
tag = st.text_input("Enter a Tag Name:")

# Ensure both inputs are non-empty
if industry and tag:  # This checks if both fields are not empty
    try:
        # Make the API call
        response = requests.get(f"http://api:4000/con/contacts/employees/{industry}/{tag}")
        # If the request was successful, parse the JSON response
        if response.status_code == 200:
            data = response.json()
            
            # If the data is in a list format, convert it to a DataFrame for easy display
            if isinstance(data, list):
                df = pd.DataFrame(data)
                st.dataframe(df)
            else:
                st.write("No contacts found or unexpected response format.")
        else:
            st.write(f"Error: Received unexpected status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        st.write(f"API error: {e}")
else:
    st.write("Please enter both an Industry and a Tag.")