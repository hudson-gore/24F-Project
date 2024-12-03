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

# Ensure the input is non-empty
if company_name:  # This checks if the input is not empty
    try:
        # Make the API call
        response = requests.get(f"http://api:4000/companies/{company_name}")
        
        # If the request was successful, parse the JSON response
        if response.status_code == 200:
            data = response.json()
            
            # If the data is in a list format, convert it to a DataFrame for easy display
            if isinstance(data, list) and data:
                df = pd.DataFrame(data)
                st.dataframe(df)  # Display the dataframe in Streamlit
            elif not data:
                st.write(f"No hiring managers found for {company_name}.")
            else:
                st.write("Unexpected response format.")
        else:
            st.write(f"Error: Received unexpected status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        st.write(f"API error: {e}")
else:
    st.write("Please enter a company name to search.")
