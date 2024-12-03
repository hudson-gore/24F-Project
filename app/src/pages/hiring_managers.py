import streamlit as st
from modules.nav import SideBarLinks
import requests

# Set page config for Streamlit
st.set_page_config(layout="wide")
SideBarLinks(show_home=True)

# Title of the page
st.title("Search for Hiring Managers")

# Add description or instructions
st.write("""
    Here you can search for hiring managers in the Accounting and Finance fields. 
    This will help you understand what skills are in demand and which companies are hiring.
""")

# Example input to search hiring managers
company_name = st.text_input("Enter a company name (e.g., Deloitte, EY):")

# Check if the user has entered a company name
if company_name:
    st.write(f"Searching for hiring managers at {company_name}...")
    
    # Call the Flask API to search for hiring managers
    try:
        # Adjust the base URL as per your Flask app's location
        response = requests.get('http://localhost:8501/hiring_managers')

        # If the API call is successful, display the results
        if response.status_code == 200:
            hiring_managers = response.json()
            for manager in hiring_managers:
                st.write(f"Name: {manager['FirstName']} {manager['LastName']}")
                st.write(f"Job Title: {manager['JobTitle']}")
                st.write(f"Company: {manager['CompanyName']}")
                st.write("---")
        else:
            st.write(response.json()['message'])  # Display error message from the API
    except Exception as e:
        st.write(f"An error occurred while fetching the data: {e}")