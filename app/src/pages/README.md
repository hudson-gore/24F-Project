# `pages` Folder

This folder contains all the pages that will be part of the application.

Pages Folder:
    The pages folder contains all the individual application pages that form the core user interface for NetWorkHub. 
    Each page is designed to demonstrate specific features and functionalities of the platform, tailored to meet the 
    needs of the different user personas: undergraduate students, hiring managers, and co-op advisors. These pages 
    aim to streamline networking, recruiting, and advising processes for all users.

Relevant Streamlit Documentation:
https://docs.streamlit.io/develop/api-reference

Home.py:
    A general landing pages providing an overview of the application and quick navigation link to user-specific sections, 
    where you are able to access one of our users, whether its a students, hiring manager or co-op advisor


1_Student_Home.py: 
    The main homepage for students. It offers buttons for navigation to student-specific functionalities such as searching 
    for internships, alumni, specific profiles, or updating their profiles to stand out more as candidates.


1_1_intern_search.py:
    Enables students searching for internships to filter by job title and industry. Provides a list of students who have 
    interened at companies matching the criteria along with their contact information and company details, facilitating 
    networking opportunities.


1_2_alumni_industry.py:
    Allows students to search for alumni based on their industry of interest. It returns a list of alumni contacts with 
    relevant details, helping students netowrk efficiently.


1_3_specific_profile.py: 
    Lets students find specific employees by searching for their employer ID for a more targeted networking approach. 
    Also enables them to add aditional tags to an employees profile registered under their user id. This page provides 
    detailed information about an indidividual's experience and contact details


2_1_alumni_search.py:
    A page that enables students to search for alumni based on specific degrees, for example aggregating a list of 
    alumni who graduated with a Accounting & Finance degree


2_2_profile_update.py:
    Allows students to update their profiles with new information regarding their status for looking for a job, 
    ensuring the database remains current and relevant. Also enables them to view their updated profile to 

    EXAMPLE INPUT:

    First Name:
        - "John"

    Last Name:
        - "Smith"

    Major:
        - "Finance"
    
    Expected Graduation Year:
        - "2026"

    Year:
        - "Junior"
    
    Profile Details:
        - "Information xyz ...."

    Phone:
        - "413-456-1234"

    Email:
        - "John_smith@gmail.com"
    
    Prfofile Manager:
        - "Terrance"

    Student Id:
        - "67"


2_3_hiring_managers.py:
    Allows students to aggregate a list of hiring managers from various companies based on the job position they 
    are looking for and industry. They are provided with a list of their contact information so they can get into 
    contact with them


2_4_add_internship.py:
    Enables authorized users to add new internship opportunities to the database for students to explore

    EXAMPLE INPUT:

    Job Title:
        - "Software Engineering Co-op"
    
    Start Date:
        - "2024/12/06"
    
    End Date:
        - "2024/12/06"
    
    Comapny:
        - "PWC"

    Student ID:
        - "124"

    Supervisor:
        - "Sara Anders"



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
    the Student Dashboard page provides co-op advisors and administrators with insights into 
    student profiles by displaying tag statistics and detailed information about students 
    associated with specific tags.


4_3_tagging_students.py:
    allows co-op advisors and other authorized users to assign descriptive tags to student profiles, 
    facilitating easier categorization and identification of students based on specific attributes or 
    qualities.

    TYPE in the desired tag, such as "hard worker", the employee id number of the tag creator,
    and enter the student id number for the student the tag is being applied to


4_4_adding_new_contacts.py:
    allows users, such as co-op advisors, to add new employee contacts to the database, 
    capturing relevant details about the employee and their association with a company.

    EXAMPLE INPUT:

        First Name:
                - "John"
        Last Name:
                - "Doe"
        Job Title:
                - "Hiring Manager"
        Profile Details:
                - "Hiring Manager @ Amazon"
        Phone:
                - [put whatever number you want to test it out]
        Email:
                - "john.doe@amazon.com"
        Degree:
                - "Business Administration"
        Contact Manager ID:
                - 6
        Profile Manager ID: 
                - 2
        Company:
                - 100


4_5_student_directory.py:
    provides users, such as co-op advisors, with a centralized interface to view and search 
    for student profiles. The directory includes functionality to list all students or search 
    for specific students by their first name

    TYPE the first name of the student you are looking for, then PRESS ENTER to see results


5_About.py:
    about page for the site describing its purpose





