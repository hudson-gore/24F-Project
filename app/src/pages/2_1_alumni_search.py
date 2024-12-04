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
  data = requests.get(f"http://api:4000/con/employees/degree/tag/{degree}/{tag}")
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)