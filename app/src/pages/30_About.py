import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    NetWorkHub is the all-in-one data-driven application connecting students 
    with professionals in their desired field of work and vice versa. Until 
    now there has not been an application that connects all the dots for students
      looking to network with alumni, current co-ops, hiring managers, or other 
      employees all in the same place. These resources exist, but students have 
      to aggregate information from LinkedIn, company websites, and databases of 
      previous co-ops. However, NetWorkHub would allow students to subset for certain 
      features/filters giving them a list of contacts which are best suited to their
        needs. Furthermore, on the other side of the same coin, how do employers know 
        they are attracting the top talent from a given university or reaching out to 
        students that could be potential fits for their entry-level/co-op roles. 
        NetWorkHub gives employers similar functionality allowing them to subset
         a database of students by certain criteria to give them a list of students 
        best suited to their needs
    """
        )
