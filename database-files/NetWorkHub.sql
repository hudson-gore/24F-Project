# Create the project database
DROP DATABASE IF EXISTS NetWorkHub;
CREATE DATABASE IF NOT EXISTS NetWorkHub;

# Check to make sure it is there
SHOW DATABASES;

# Use the NetWorkHub Database
USE NetWorkHub;

# Create parent table for all people
CREATE TABLE people(
    ID INT PRIMARY KEY AUTO_INCREMENT
);

# Create the Advisors Table
CREATE TABLE advisors(
    AdvisorID INT PRIMARY KEY,
    FirstName varchar(50),
    LastName varchar(50),
    Email varchar(50),
    Phone varchar(50),
    FOREIGN KEY (AdvisorID) REFERENCES people(ID)
        ON UPDATE cascade ON DELETE restrict
);

# Create the Students table
CREATE TABLE students(
    StudentID INT PRIMARY KEY,
    FirstName varchar(50),
    LastName varchar(50),
    Major varchar(50),
    Minor varchar(50),
    ExpectedGrad INT NOT NULL,
    Year varchar(30),
    ProfileDetails text,
    Phone varchar(50),
    Email varchar(50),
    ProfileManager INT NOT NULL,
    FOREIGN KEY (ProfileManager) REFERENCES advisors(AdvisorID)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (StudentID) REFERENCES people(ID)
        ON UPDATE cascade ON DELETE restrict
);

# Create the Companies Table
CREATE TABLE companies(
    CompanyID INT PRIMARY KEY AUTO_INCREMENT,
    CompanyName varchar(50),
    Industry varchar(100),
    Location varchar(50),
    Size INT,
    ProfileManager INT NOT NULL,
    FOREIGN KEY (ProfileManager) REFERENCES advisors(AdvisorID)
        ON UPDATE cascade ON DELETE restrict
);

# Create the Employees Table
CREATE TABLE employees(
    EmployeeID INT PRIMARY KEY,
    FirstName varchar(50),
    LastName varchar(50),
    JobTitle varchar(100),
    ProfileDetails text,
    Phone varchar(50),
    Email varchar(50),
    Degree varchar(100),
    ContactManager INT NOT NULL,
    ProfileManager INT NOT NULL,
    Company INT NOT NULL,
    FOREIGN KEY (ContactManager) REFERENCES employees(EmployeeID)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (ProfileManager) REFERENCES advisors(AdvisorID)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (Company) REFERENCES companies(CompanyID)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (EmployeeID) REFERENCES people(ID)
        ON UPDATE cascade ON DELETE restrict
);

# Create the Tags table
CREATE TABLE tags(
    TagID INT PRIMARY KEY AUTO_INCREMENT,
    TagName varchar(100) NOT NULL,
    TagOwner INT NOT NULL,
    TaggedUser INT NOT NULL,
    FOREIGN KEY (TagOwner) REFERENCES people(ID)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (TaggedUser) REFERENCES people(ID)
        ON UPDATE cascade ON DELETE restrict
);

# Create the Co-op/Internships table
CREATE TABLE internships(
    PositionID INT PRIMARY KEY AUTO_INCREMENT,
    JobTitle varchar(50) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Company INT NOT NULL,
    PositionHolder INT NOT NULL,
    Supervisor INT NOT NULL,
    FOREIGN KEY (Company) REFERENCES companies(CompanyID)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (PositionHolder) REFERENCES  people(ID)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (Supervisor) REFERENCES employees(EmployeeID)
        ON UPDATE cascade ON DELETE restrict
);

# Insert some people in the database
INSERT INTO people(ID)
VALUES(1),(2),(3),(4),(5), (6), (7);

# Insert two advisors in the advisors table
INSERT INTO advisors(AdvisorID, FirstName, LastName, Email, Phone)
VALUES (1,'Sarah', 'Patel', 's.patel@northeastern.edu', '(555) 947-8231'),
       (2,'Samantha', 'Keller', 's.keller@northeastern.edu', '(555) 238-7641');

# Insert two students in the student table
INSERT INTO students(StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails,
                     Phone, Email, ProfileManager)
VALUES (3, 'Jordan', 'Thompson', 'Computer Science', 'Applied Mathematics',
        2026, 'Third', 'Jordan Thompson - Comp Sci & Applied Mathematics',
        '(555) 712-4398', 'thompson.j@northeastern.edu', 1),
        (4, 'Maya', 'Chen', 'Accounting & Finance',NULL, 2025,
        'Fourth', 'Graduating in the Spring and looking for full time opportunities',
        '(555) 864-3270', 'chen.m@northeastern.edu', 2);

# Insert two companies into the companies table
INSERT INTO companies(CompanyID, CompanyName, Industry, Location, Size, ProfileManager)
VALUES (100, 'Amazon', 'Tech', 'Seattle', 1000000,
        1),
        (101, 'PWC', 'Accounting', 'London', 370000,
         2),
        (102, 'Wayfair', 'Retail', 'Boston', 14400,
         2);

# Insert two employees into the employees table
INSERT INTO employees(EmployeeID, FirstName, LastName, JobTitle, ProfileDetails, Phone, Email,
                      Degree, ContactManager, ProfileManager, Company)
VALUES (5, 'Alex', 'Rivera', 'Hiring Manager',
        'I am the Hiring Manager for Wayfairs Northeastern Co-ops', '(555) 392-1684',
        'arivera@wayfair.com','Communications', 5, 1, 102),
        (6, 'Michael', 'Roberts', 'Senior Consultant, Advisory Services',
         'Senior Consultant @ PWC', '(555) 473-9261', 'michael.roberts@pwc.com',
         'Accounting & Finance', 6, 2, 101),
        (7, 'Emily', 'Carter', 'Software Engineer',
         'Software Engineer @ SWE', '(555) 742-6159', 'ecarter@wayfair.com',
         'Computer Science', 5, 1, 102);

# Insert two tags into the tags table
INSERT INTO tags(TagID, TagName, TagOwner, TaggedUser)
VALUES (1, 'Alumni', 1, 6),
       (2, 'Candidates', 5,3);

# Insert two positions into the internships table
INSERT INTO internships(PositionID, JobTitle, StartDate, EndDate, Company, PositionHolder, Supervisor)
VALUES (1, 'Accounting Co-op', '2023-7-10', '2023-12-22', 101,
        4, 6),
        (2, 'Software Engineer Co-op', '2022-7-10', '2023-12-22', 102,
         7, 7);


