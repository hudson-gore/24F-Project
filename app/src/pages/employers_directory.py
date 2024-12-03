import streamlit as st
from modules.nav import SideBarLinks
# Page configuration
st.set_page_config(layout="wide")
SideBarLinks(show_home=True)

# Title for the page
st.title("Employers Directory")

# Description
st.write("""
    Use this page to update/delete employers listings.
""")

# Example input to search Employers
industry = st.text_input("Enter an Industry Name:")
tag = st.text_input("Comapny Name:")

print(industry, tag )

with st.expander("Role Type"):
    roles = st.multiselect(
        "Select Job Listings Looking For", ["Software Engineer", "Data Analyst", "Cloud Engineer", "QRole", "IT"], default=["Software Engineer"]
    )
    st.write(f"Selected {len(roles)}/5")

# Ensure both inputs are non-empty
if industry and tag:  # This checks if both fields are not empty
    try:
        # Make the API call
        response = requests.get(f"http://api:4000/con/contacts/industry/tag/{industry}/{tag}")
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




