import streamlit as st
import requests

# Function to get all company names
def get_all_companies():
    try:
        response = requests.get("http://api:4000/com/companies")
        if response.status_code == 200:
            companies = response.json()
            # Extract company names from the response
            return [c['CompanyName'] for c in companies]
        else:
            st.error("Error fetching company names from the database.")
            return []
    except Exception as e:
        st.error(f"An error occurred while fetching companies: {e}")
        return []

# Function to delete a company profile
def delete_company(company_name):
    try:
        response = requests.delete(f"http://api:4000/com/companies/{company_name}")
        if response.status_code == 200:
            st.success(f"Successfully deleted the company profile for '{company_name}'.")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit app title
st.title("Manage Company Profiles")

# Fetch and display the dropdown menu with all company names
companies = get_all_companies()

if companies:
    selected_company = st.selectbox("Select a company to delete:", companies)

    if st.button("Delete Company"):
        delete_company(selected_company)
else:
    st.warning("No companies found in the database.")
