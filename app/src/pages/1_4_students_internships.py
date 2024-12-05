import streamlit as st
import requests
import pandas as pd

# Function to get all available companies from the database
def get_companies():
    try:
        response = requests.get("http://api:4000/com/companies/internships")
        if response.status_code == 200:
            return response.json() 
        else:
            st.error("Error fetching companies from the database.")
            return []
    except Exception as e:
        st.error(f"An error occurred while fetching companies: {e}")
        return []

# Function to get all available positions from the database for a specific company
def get_positions(company_name):
    try:
        response = requests.get(f"http://api:4000/i/internships/pos/comp/{company_name}")
        if response.status_code == 200:
            return response.json()  
        else:
            st.error(f"Error fetching positions for {company_name}.")
            return []
    except Exception as e:
        st.error(f"An error occurred while fetching positions: {e}")
        return []

# Streamlit app title
st.title("Students by Co-op Position")

# Get companies from the database
companies = get_companies()

# Display the dropdown menu for selecting the company
if companies:
    # Assuming the company names are in a field called 'CompanyName'
    company_names = [company['CompanyName'] for company in companies] 
    company = st.selectbox("Select Company:", company_names)
else:
    st.warning("No companies found in the database.")

# Display the dropdown menu for selecting the position, but only if a company is selected
if company:
    positions = get_positions(company)
    if positions:
        # Assuming the position titles are in a field called 'JobTitle'
        position_titles = [position['JobTitle'] for position in positions]  
        position = st.selectbox("Select Position:", position_titles)
    else:
        st.warning(f"No positions found for {company}.")
else:
    position = None  
    
# Submit button
if st.button("Search") and company and position:
    try:
        # Construct API URL
        api_url = f"http://api:4000/con/contacts/students/{company}/{position}"
        # Make the GET request
        response = requests.get(api_url)
        
        if response.status_code == 200:
            # Convert JSON response to DataFrame
            data = response.json()
            if data:
                df = pd.DataFrame(data, columns=["FirstName", "LastName", "Email", "Phone"])
                # Display results
                st.write(f"Students who held the position '{position}' at {company}:")
                st.dataframe(df)
            else:
                st.warning(f"No students found for the position '{position}' at {company}.")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    # Show warning if either company or position are not selected
    if not company:
        st.warning("Please select a Company.")
    elif not position:
        st.warning("Please select a Position.")
