# `pages` Folder

This folder contains all the pages that will be part of the application. Details on required numbers will be provided in the Phase 3 documentation.

These pages are meant to show you an example of some of the features of Streamlit and the way we will limit functionality access by role/persona. It is not meant to represent a complete application.

TODO: Describe the pages folder and include link to documentation. Don't forget about ordering of pages.


Home.py:


1_Student_Home.py: 


1_1_intern_search.py:


1_2_alumni_industry.py:


1_3_specific_profile.py: 


2_1_alumni_search.py:


2_2_profile_update.py:


2_3_hiring_managers.py:


2_4_add_internship.py:


3_Hiring_Mangager_Home.py:
    the Hiring Manager Home Page within the broader NetWorkHub platform. It provides a personalized 
    interface for hiring managers to access tools and resources for managing co-op students and maintaining 
    relationships between their organization and Northeastern University.
    
    CLICK one of the 4 buttons to see the features available to this user.


3_1_student_tags.py:
    this defines the Students by Tag page within the broader NetWorkHub platform. The page allows users,
    such as hiring managers or advisors, to search for students based on specific tags stored in the database. 
    The results are dynamically fetched and displayed in an interactive table.

    CLICK on the dropdown menu below "Select Tag:", then click search to see results. 
    or
    TYPE a valid tag name into the field and click search to see results. 


3_2_dashboard.py:
    it provides hiring managers with visual insights into the student population based on their academic 
    major and year, as well as a detailed list of all students in the database.


3_3_add_profile.py:
    users to create and manage employee profiles in the NetWorkHub platform. It provides a user-friendly form 
    to submit employee data to the database, retrieve individual profiles, and view all employee profiles for 
    a specific company.

    EXAMPLE INPUT:

        First Name:
                - "John"
        Last Name:
                - "Doe"
        Job Title:
                - "Hiring Manager"
        Profile Details:
                - "Hiring Manager @ PWC"
        Phone:
                - [put whatever number you want to test it out]
        Email:
                - "john.doe@pwc.com"
        Contact Manager:
                - 6
        Profile Manager:
                - 2
        Company:
                - 101 (pwc)
        EmployeeID:
                - [put any number you want that is >1000 to avoid conflicts with existing IDs in database]


3_4_delete_profile.py:
    the Delete Profile page, part of the NetWorkHub platform. It allows users, specifically Alex at 
    Wayfair, to view and manage employee profiles associated with Wayfair. Users can select a contact 
    to delete from a dropdown menu and view an updated list of contacts after deletion.

    CLICK on a contact from the drop down menu
    or 
    TYPE in the name of a contact

    then, CLICK the "Delete Contact" button below

    You can view the the current contacts by clicking the "Show Updated Contacts"
    - you can click this before removing a contact to see current list, then after to see that 
      the deleted individual has been removed


4_Advisor_Home.py:
    Advisor Home Page for the NetWorkHub platform. It serves as the main dashboard for co-op 
    advisors, such as Dr. Sarah Patel, providing tools and resources to manage student 
    relationships, applications, and employer contacts.


4_1_delete_company.py:
    the Manage Company Profiles page for the NetWorkHub platform. It enables users, such as 
    co-op advisors, to view a list of all companies in the database and delete company profiles 
    when necessary. This page is designed to maintain an up-to-date and accurate database by 
    removing severed or outdated company relationships.

    CLICK on the dropdown menu to and CLICK on a company
    or 
    TYPE the name of a valid company

    CLICK "Delete Company" button to remove the company


4_2_application_dashboard.py:


4_3_tagging_students.py:


4_4_adding_new_contacts.py:


4_5_student_directory.py:


5_About.py:






