import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Function to get all students from the database
def get_students():
    try:
        response = requests.get("http://api:4000/con/contacts/students") 
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Error fetching students from the database.")
            return []
    except Exception as e:
        st.error(f"An error occurred while fetching students: {e}")
        return []

# Streamlit app title
st.title("Hiring Manager Dashboard")

# Get all students from the database
students = get_students()

# If students data is available
if students:
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(students)

    # Creating subplots for Pie Charts to be stacked side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns

    # Displaying Pie Chart for Students by Major
    st.subheader("Student Distribution")
    major_counts = df['Major'].value_counts()
    ax1.pie(major_counts, labels=None, autopct='%1.1f%%', startangle=90) 
    ax1.axis('equal')  # Equal aspect ratio ensures the pie chart is drawn as a circle.
    ax1.set_title("Distribution by Major")
    ax1.legend(major_counts.index, loc="center", bbox_to_anchor=(0.5, -0.2), ncol=3)

    # Displaying Pie Chart for Students by Year
    year_counts = df['Year'].value_counts()
    ax2.pie(year_counts, labels=None, autopct='%1.1f%%', startangle=90)  
    ax2.axis('equal')
    ax2.set_title("Distribution by Year")
    ax2.legend(year_counts.index, loc="center", bbox_to_anchor=(0.5, -0.2), ncol=3)

    # Display the side-by-side pie charts
    st.pyplot(fig)

    # Displaying List of Students
    st.subheader("List of All Students")
    st.dataframe(df[['FirstName', 'LastName', 'Year', 'Major', 'Email', 'Phone']])

else:
    st.warning("No student data found in the database.")
