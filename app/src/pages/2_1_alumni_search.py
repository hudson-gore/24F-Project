import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Set page config for Streamlit
st.set_page_config(layout="wide")
SideBarLinks(show_home=True)

# Title of the page
st.title("Alumni Who Graduated with Accounting & Finance Degree")

# Inputs
degree = 'Accounting & Finance'
tag = 'Alumni'


# Make the api call
data = {} 
try:
    response = requests.get(f"http://api:4000/con/contacts/employees/degree/tag/{degree}/{tag}")
    response.raise_for_status()  # Ensure HTTP errors are caught
    data = response.json()
    if isinstance(data, list) and data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.write("No data available for the selected criteria.")
except Exception as e:
    st.write(f"Error fetching data: {e}")

#st.dataframe(data)