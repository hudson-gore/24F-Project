# `database-files` Folder
Ryan Devlin, Hudson Gore, Aman Bhojwani, Maximilian Hill, Issa Kabore
1) Data Base Creation:
    - The sql file first drops the database if it exists and creates a fresh one named NetWorkHub
    - This ensurees a clean slate from the database

2) Using the Database:
    - The sql file uses USE NetWorkHub to ensure all operations apply to the NetWorkHub database

3) Table Definitons:
    - In the file the scheme for various tables is defined, these include:
        - advisors
        - students
        - companies 
        - employees
        - employee_tags
        - student_tags
        - internships

    - it also includes relationships between tables using foreign keys with cascading rules (ON UPDATE CASCADE, ON DELETE RESTRICT)

4) Inserting Data
    - After defining the scheme, serveral data points are inserted into each table of the databse with the initial data fro advisors, students, companies, employees and their relationships

5) Constraints:
    - Foreign keys help ensure data integrity across tables for example: ProfileManager in students references AdvisorID in the advisors table


How to Reboot the Data Base:

1) Drop and Recreate the Database
    - Execute the first part of the script:
        - DROP DATABASE IF EXISTS NetWorkHub;
        - CREATE DATABASE IF NOT EXISTS NetWorkHub;
        - USE NetWorkHub;
    - This ensures the previous database is removed, and a new, clean database is created.

2) Create Tables
    - Run the section of the script that defines the tables:
    - Ensure primary keys are defined as well as foreign keys to ensure the links between the tables
        - CREATE TABLE advisors (...);
        - CREATE TABLE students (...);
        - CREATE TABLE companies (...);
        - CREATE TABLE employees (...);
        - CREATE TABLE employee_tags (...);
        - CREATE TABLE student_tags (...);
        - CREATE TABLE internships (...);

3) Insert Initial Data
    - Populate the database with the pre-defined data provided in the script:
        - INSERT INTO advisors (...);
        - INSERT INTO students (...);
        - INSERT INTO companies (...);
        - INSERT INTO employees (...);
        - INSERT INTO employee_tags (...);
        - INSERT INTO student_tags (...);
        - INSERT INTO internships (...);

4) Verify the Database
    - Use commands like SHOW TABLES; or SELECT * FROM <table_name>; to verify that tables are created and data is inserted correctly.