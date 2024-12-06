# Create the project database
DROP DATABASE IF EXISTS NetWorkHub;
CREATE DATABASE IF NOT EXISTS NetWorkHub;

# Check to make sure it is there
SHOW DATABASES;

# Use the NetWorkHub Database
USE NetWorkHub;

# Create the Advisors Table
CREATE TABLE advisors(
    AdvisorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName varchar(50),
    LastName varchar(50),
    Email varchar(50),
    Phone varchar(50)
);

# Create the Students table
CREATE TABLE students(
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName varchar(50),
    LastName varchar(50),
    Major varchar(50),
    Minor varchar(50),
    ExpectedGrad INT NOT NULL,
    Year varchar(30),
    ProfileDetails text,
    Phone varchar(50),
    Email varchar(50),
    ProfileManager INT,
    FOREIGN KEY (ProfileManager) REFERENCES advisors(AdvisorID)
        ON UPDATE cascade ON DELETE SET NULL
);

# Create the Companies Table
CREATE TABLE companies(
    CompanyID INT PRIMARY KEY AUTO_INCREMENT,
    CompanyName varchar(50),
    Industry varchar(100),
    Location varchar(50),
    Size INT,
    ProfileManager INT,
    FOREIGN KEY (ProfileManager) REFERENCES advisors(AdvisorID)
        ON UPDATE cascade ON DELETE SET NULL
);

# Create the Employees Table
CREATE TABLE employees(
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName varchar(50),
    LastName varchar(50),
    JobTitle varchar(100),
    ProfileDetails text,
    Phone varchar(50),
    Email varchar(50),
    Degree varchar(100),
    ContactManager INT,
    ProfileManager INT,
    Company INT NOT NULL,
    FOREIGN KEY (ContactManager) REFERENCES employees(EmployeeID)
        ON UPDATE cascade ON DELETE SET NULL,
    FOREIGN KEY (ProfileManager) REFERENCES advisors(AdvisorID)
        ON UPDATE cascade ON DELETE SET NULL,
    FOREIGN KEY (Company) REFERENCES companies(CompanyID)
        ON UPDATE cascade ON DELETE cascade, 
);

# Create the Employee Tags table
CREATE TABLE employee_tags(
    TagID INT PRIMARY KEY AUTO_INCREMENT,
    TagName varchar(100) NOT NULL,
    TagOwner INT NOT NULL,
    TaggedUser INT NOT NULL,
    FOREIGN KEY (TagOwner) REFERENCES employees(EmployeeID)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (TaggedUser) REFERENCES students(StudentID)
        ON UPDATE cascade ON DELETE cascade
);

# Create the Student Tags table
CREATE TABLE student_tags(
    TagID INT PRIMARY KEY AUTO_INCREMENT,
    TagName varchar(100) NOT NULL,
    TagOwner INT NOT NULL,
    TaggedUser INT NOT NULL,
    FOREIGN KEY (TagOwner) REFERENCES students(StudentID)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (TaggedUser) REFERENCES employees(EmployeeID)
        ON UPDATE cascade ON DELETE cascade
);

# Create the Co-op/Internships table
CREATE TABLE internships(
    PositionID INT PRIMARY KEY AUTO_INCREMENT,
    JobTitle varchar(50) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Company INT NOT NULL,
    PositionHolder INT NOT NULL,
    Supervisor INT NOT,
    FOREIGN KEY (Company) REFERENCES companies(CompanyID)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (PositionHolder) REFERENCES  students(StudentID)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (Supervisor) REFERENCES employees(EmployeeID)
        ON UPDATE cascade ON DELETE SET NULL
);

# Insert Advisors
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (1, 'Sarah', 'Patel', 'spatel@northeastern.edu', '385-622-8096');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (2, 'Rodger', 'Kiddle', 'rkiddle1@stanford.edu', '185-571-7664');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (3, 'Carney', 'Rosone', 'crosone2@geocities.jp', '567-716-8697');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (4, 'Hugh', 'Bonhan', 'hbonhan3@mlb.com', '585-316-7160');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (5, 'Danya', 'Zamora', 'dzamora4@altervista.org', '838-166-6408');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (6, 'Kendrick', 'Rothermel', 'krothermel5@washingtonpost.com', '685-470-3194');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (7, 'Darren', 'Roll', 'droll6@comcast.net', '600-758-7402');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (8, 'Paige', 'Hanwell', 'phanwell7@yahoo.com', '761-514-0003');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (9, 'Lib', 'Josephson', 'ljosephson8@weather.com', '210-170-3098');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (10, 'Haley', 'Paddington', 'hpaddington9@1und1.de', '382-732-2552');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (11, 'Bear', 'Gabbett', 'bgabbetta@shutterfly.com', '891-741-6171');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (12, 'Loralyn', 'Gerbl', 'lgerblb@github.io', '973-987-5031');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (13, 'Petr', 'Skyppe', 'pskyppec@biglobe.ne.jp', '788-324-6756');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (14, 'Stevy', 'Metherell', 'smetherelld@networkadvertising.org', '310-429-2136');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (15, 'Joly', 'McCowen', 'jmccowene@home.pl', '805-792-2176');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (16, 'Amara', 'Bullerwell', 'abullerwellf@jiathis.com', '901-576-8234');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (17, 'Sherwin', 'Lesmonde', 'slesmondeg@netscape.com', '765-944-8683');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (18, 'Amii', 'Buttler', 'abuttlerh@mapy.cz', '519-810-1505');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (19, 'Etan', 'Perryn', 'eperryni@diigo.com', '575-399-4500');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (20, 'Angela', 'Durnin', 'adurninj@webmd.com', '609-215-7239');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (21, 'Sibyl', 'Leithgoe', 'sleithgoek@unblog.fr', '787-966-9459');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (22, 'Zenia', 'Redwood', 'zredwoodl@shareasale.com', '434-201-0731');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (23, 'Doloritas', 'Studman', 'dstudmanm@forbes.com', '632-416-9362');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (24, 'Ellerey', 'Straniero', 'estranieron@java.com', '774-378-1753');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (25, 'Zebedee', 'Seally', 'zseallyo@apple.com', '843-673-0145');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (26, 'Melanie', 'Samwaye', 'msamwayep@netscape.com', '917-899-7945');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (27, 'Elnora', 'Antonelli', 'eantonelliq@youtube.com', '186-135-9356');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (28, 'Casar', 'Postins', 'cpostinsr@ibm.com', '444-180-4423');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (29, 'Jase', 'Tritten', 'jtrittens@cyberchimps.com', '854-133-7760');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (30, 'Doralia', 'Comettoi', 'dcomettoit@barnesandnoble.com', '153-718-0097');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (31, 'Corrie', 'Breewood', 'cbreewoodu@cdc.gov', '734-990-9198');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (32, 'Keefe', 'Flindall', 'kflindallv@toplist.cz', '579-177-0850');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (33, 'Cherise', 'Penny', 'cpennyw@woothemes.com', '201-345-3041');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (34, 'Madella', 'Balharrie', 'mbalharriex@kickstarter.com', '185-825-2187');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (35, 'Beth', 'Garry', 'bgarryy@usa.gov', '512-515-0234');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (36, 'Berty', 'Bails', 'bbailsz@unblog.fr', '460-757-5912');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (37, 'Cherye', 'Celier', 'ccelier10@nymag.com', '868-698-5111');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (38, 'Cayla', 'Meatcher', 'cmeatcher11@hatena.ne.jp', '492-523-6585');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (39, 'Georges', 'Lidgertwood', 'glidgertwood12@illinois.edu', '352-180-9583');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (40, 'Lucila', 'Blinco', 'lblinco13@engadget.com', '555-341-2897');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (41, 'Arny', 'Boshard', 'aboshard14@dot.gov', '779-805-1278');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (42, 'Cherida', 'Bamell', 'cbamell15@dell.com', '154-973-0037');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (43, 'Danny', 'Jellyman', 'djellyman16@yelp.com', '719-460-1365');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (44, 'Jocelin', 'Goslin', 'jgoslin17@fc2.com', '291-411-8743');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (45, 'Dotti', 'Heaysman', 'dheaysman18@bing.com', '347-279-7271');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (46, 'Freda', 'Stammler', 'fstammler19@yellowbook.com', '200-427-2960');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (47, 'Sumner', 'Gohn', 'sgohn1a@wordpress.org', '294-322-2067');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (48, 'Ariana', 'Burleigh', 'aburleigh1b@yahoo.com', '957-195-0326');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (49, 'Aurelie', 'Olivello', 'aolivello1c@telegraph.co.uk', '114-972-5449');
insert into advisors (AdvisorID, FirstName, LastName, Email, Phone) values (50, 'Kaila', 'Gillian', 'kgillian1d@elpais.com', '652-763-1417');

# Insert Students
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (1, 'Paxton', 'Ornillos', 'Accounting', 'Sociology', 2027, 'Second', 'Coffee lover', '601-132-3302', 'pornillos0@geocities.jp', 1);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (2, 'Francene', 'Doulton', 'Psychology', 'Music Theory', 2028, 'Second', 'Guitar player', '391-732-7210', 'fdoulton1@myspace.com', 2);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (3, 'Ryann', 'Marzello', 'Accounting', 'Fashion Design', 2028, 'Second', 'Traveler', '534-405-1316', 'rmarzello2@xrea.com', 3);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (4, 'Neile', 'Sammon', 'Accounting', 'Gender Studies', 2025, 'Second', 'Guitar player', '281-280-7932', 'nsammon3@dmoz.org', 4);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (5, 'Grace', 'Gemmill', 'Political Science', 'Psychology', 2028, 'Third', 'Male', '878-768-8495', 'ggemmill4@nytimes.com', 5);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (6, 'Elihu', 'McIlwreath', 'Computer Science', 'Creative Writing', 2026, 'First', 'Software Engineer', '699-833-0954', 'emcilwreath5@xinhuanet.com', 6);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (7, 'Hewet', 'Galton', 'Mechanical Engineering', 'Film Studies', 2024, 'Fourth', 'Male', '240-955-0239', 'hgalton6@drupal.org', 7);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (8, 'Maribeth', 'Johns', 'Software Engineer', 'Psychology', 2029, 'Fourth', '25 years old', '812-889-3781', 'mjohns7@linkedin.com', 8);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (9, 'Beale', 'Garlee', 'Sociology', 'Dance', 2025, 'Second', 'Hiking enthusiast', '535-170-9185', 'bgarlee8@imgur.com', 9);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (10, 'Archer', 'Brinded', 'Mechanical Engineering', 'Urban Planning', 2024, 'Third', 'Fluent in Spanish', '157-803-0456', 'abrinded9@quantcast.com', 10);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (11, 'Rolfe', 'Banker', 'Biology', 'Public Health', 2028, 'First', 'Coffee lover', '430-965-3029', 'rbankera@loc.gov', 11);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (12, 'Marcile', 'Poytres', 'Chemistry', 'Psychology', 2029, 'Fourth', 'Guitar player', '864-744-0690', 'mpoytresb@hc360.com', 12);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (13, 'Simonette', 'Mirralls', 'Computer Science', 'Music Theory', 2027, 'First', 'New York', '511-840-2190', 'smirrallsc@furl.net', 13);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (14, 'Tony', 'Cretney', 'Chemistry', 'Nutrition', 2026, 'Third', 'Traveler', '581-606-5326', 'tcretneyd@omniture.com', 14);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (15, 'Delainey', 'Mathie', 'Accounting', 'Criminology', 2024, 'Fourth', '25 years old', '725-823-8542', 'dmathiee@naver.com', 15);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (16, 'Melba', 'Grumell', 'Sociology', 'Dance', 2028, 'Second', 'NY', '656-580-7595', 'mgrumellf@prlog.org', 16);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (17, 'Petronilla', 'Edgson', 'Political Science', 'Psychology', 2025, 'Third', 'Guitar player', '530-984-8589', 'pedgsong@g.co', 17);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (18, 'Beale', 'Sherbrooke', 'Psychology', 'Urban Planning', 2029, 'Fourth', 'Guitar player', '664-753-2529', 'bsherbrookeh@census.gov', 18);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (19, 'Shaughn', 'Greenset', 'Accounting', 'Environmental Studies', 2024, 'First', 'Coffee lover', '648-916-1753', 'sgreenseti@taobao.com', 19);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (20, 'Brigida', 'O''Heaney', 'Software Engineer', 'Public Health', 2027, 'First', 'John Doe', '144-376-5060', 'boheaneyj@globo.com', 20);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (21, 'Pall', 'Blaszczak', 'Computer Science', 'Film Studies', 2028, 'Second', 'Guitar player', '797-725-4080', 'pblaszczakk@sina.com.cn', 21);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (22, 'Tito', 'McKelvie', 'English Literature', 'Urban Planning', 2024, 'First', 'Male', '997-664-0823', 'tmckelviel@desdev.cn', 22);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (23, 'Adelind', 'Langlais', 'Sociology', 'Film Studies', 2025, 'First', 'Software Engineer', '341-425-1668', 'alanglaism@mit.edu', 23);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (24, 'Boyce', 'Syratt', 'Political Science', 'Creative Writing', 2025, 'Third', 'New York', '695-302-4669', 'bsyrattn@abc.net.au', 24);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (25, 'Anatol', 'Beavis', 'Sociology', 'Anthropology', 2024, 'First', 'Software Engineer', '609-268-3895', 'abeaviso@bloglovin.com', 25);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (26, 'Maryjo', 'Slemmonds', 'Art History', 'Psychology', 2026, 'Third', 'New York', '940-597-4486', 'mslemmondsp@time.com', 26);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (27, 'Justine', 'Colebeck', 'Art History', 'Criminology', 2029, 'Second', 'Traveler', '402-307-9001', 'jcolebeckq@ow.ly', 27);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (28, 'Zaccaria', 'Beales', 'Sociology', 'Criminology', 2025, 'Third', 'Hiking enthusiast', '583-311-2723', 'zbealesr@de.vu', 28);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (29, 'Jerri', 'Wehnerr', 'Business Administration', 'Computer Science', 2024, 'Third', 'NY', '827-575-7001', 'jwehnerrs@bizjournals.com', 29);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (30, 'Robbin', 'Storkes', 'Biology', 'Criminology', 2026, 'First', 'Male', '471-359-5647', 'rstorkest@vinaora.com', 30);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (31, 'Fina', 'Langston', 'Political Science', 'Music Theory', 2028, 'First', 'Hiking enthusiast', '156-989-8758', 'flangstonu@privacy.gov.au', 31);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (32, 'Marcelia', 'Snewin', 'Software Engineer', 'Sociology', 2024, 'Second', 'Traveler', '610-738-7809', 'msnewinv@stumbleupon.com', 32);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (33, 'Bond', 'Gonzalez', 'English Literature', 'Environmental Studies', 2025, 'Second', 'NY', '282-372-2661', 'bgonzalezw@omniture.com', 33);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (34, 'Melitta', 'Hallawell', 'Sociology', 'Environmental Studies', 2028, 'Third', 'Fluent in Spanish', '325-815-0914', 'mhallawellx@thetimes.co.uk', 34);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (35, 'Gerti', 'Odby', 'Software Engineer', 'Film Studies', 2029, 'Second', 'Male', '770-888-0042', 'godbyy@slashdot.org', 35);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (36, 'Trixi', 'Reyna', 'Computer Science', 'Urban Planning', 2026, 'First', 'Coffee lover', '461-448-3784', 'treynaz@spotify.com', 36);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (37, 'Carmencita', 'Cowburn', 'Psychology', 'Nutrition', 2026, 'First', 'Software Engineer', '445-540-6360', 'ccowburn10@state.tx.us', 37);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (38, 'Helge', 'Semens', 'Political Science', 'Urban Planning', 2028, 'Second', 'Software Engineer', '999-370-5513', 'hsemens11@wordpress.com', 38);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (39, 'Gale', 'Mordacai', 'Political Science', 'Music Theory', 2025, 'Fourth', 'Software Engineer', '329-966-4282', 'gmordacai12@usda.gov', 39);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (40, 'Edithe', 'Jacobsson', 'Business Administration', 'Creative Writing', 2025, 'First', 'NY', '796-321-8546', 'ejacobsson13@furl.net', 40);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (41, 'Isac', 'Stebbing', 'Art History', 'Dance', 2029, 'Fourth', 'Hiking enthusiast', '160-234-6129', 'istebbing14@ed.gov', 41);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (42, 'Ulla', 'Hotton', 'Political Science', 'Environmental Studies', 2025, 'First', 'Coffee lover', '923-731-4650', 'uhotton15@is.gd', 42);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (43, 'Doti', 'Campe', 'Chemistry', 'Psychology', 2028, 'First', 'Hiking enthusiast', '315-498-5982', 'dcampe16@bbb.org', 43);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (44, 'Jacques', 'Ranyelld', 'Biology', 'Music Theory', 2028, 'Fourth', 'Software Engineer', '910-906-0572', 'jranyelld17@vk.com', 44);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (45, 'Aurelea', 'Pyner', 'Sociology', 'Music Theory', 2027, 'Fourth', 'Coffee lover', '314-697-9295', 'apyner18@ft.com', 45);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (46, 'Karyl', 'Ridewood', 'Biology', 'Urban Planning', 2026, 'Second', 'NY', '571-570-9942', 'kridewood19@surveymonkey.com', 46);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (47, 'Kevan', 'Keers', 'Business Administration', 'Public Health', 2028, 'Second', '25 years old', '971-657-9339', 'kkeers1a@edublogs.org', 47);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (48, 'Ariadne', 'Danforth', 'Art History', 'Psychology', 2024, 'Third', 'Fluent in Spanish', '363-172-2910', 'adanforth1b@a8.net', 48);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (49, 'Maya', 'Chen', 'Accounting & Finance', 'Gender Studies', 2025, 'Fourth', 'Looking for full time role!', '398-740-0252', 'meate1c@jiathis.com', 49);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (50, 'Jordan', 'Thompson', 'Computer Science', 'Applied Math', 2026, 'Second', 'Fluent in Spanish', '938-386-6627', 'npantlin1d@google.fr', 50);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (51, 'Emma', 'Foster', 'Computer Science', 'Psychology', 2025, 'Fourth', 'Minimalist designer, tech enthusiast, creative visionary', '555-812-3490', 'emma.foster@mail.com', 1);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (52, 'James', 'Holloway', 'Computer Science', 'Sociology', 2026, 'Third', 'AI engineer, problem solver, innovation seeker', '555-874-1293', 'james.holloway@gmail.com', 2);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (53, 'Olivia', 'Carter', 'Computer Science', 'Philosophy', 2027, 'Second', 'Finance enthusiast, socially responsible, entrepreneurial spirit', '555-563-2417', 'olivia.carter@outlook.com', 3);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (54, 'Noah', 'Turner', 'Computer Science', 'Environmental Studies', 2028, 'First', 'Environmental advocate, biology student, sustainability-driven', '555-482-3561', 'noah.turner@edu.org', 4);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (55, 'Isabella', 'Mitchell', 'Computer Science', 'Business', 2027, 'Second', "Writer, poet, capturing life's moments", '555-219-8476', 'isabella.mitchell@mail.net', 5);
insert into students (StudentID, FirstName, LastName, Major, Minor, ExpectedGrad, Year, ProfileDetails, Phone, Email, ProfileManager) values (56, 'Liam', 'Bennett', 'Computer Science', 'Yoga', 2026, 'Third', 'History lover, future educator, knowledge seeker', '555-738-9924', 'liam.bennet@biz.com', 6);

# Insert two companies into the companies table
INSERT INTO companies (CompanyID, CompanyName, Industry, Location, Size, ProfileManager) VALUES
(1, 'Apple', 'Tech', 'Cupertino, CA', 147000, 1),
(2, 'Microsoft', 'Technology', 'Redmond, WA', 221000, 2),
(3, 'Amazon', 'E-Commerce', 'Seattle, WA', 1600000, 3),
(4, 'Tesla', 'Automotive', 'Palo Alto, CA', 70000, 4),
(5, 'Google', 'Tech', 'Mountain View, CA', 156500, 5),
(6, 'Facebook', 'Tech', 'Menlo Park, CA', 58604, 6),
(7, 'Coca-Cola', 'Beverages', 'Atlanta, GA', 86200, 7),
(8, 'PepsiCo', 'Beverages', 'Purchase, NY', 291000, 8),
(9, 'Walmart', 'Retail', 'Bentonville, AR', 2300000, 9),
(10, 'Intel', 'Semiconductors', 'Santa Clara, CA', 121100, 10),
(11, 'Nike', 'Apparel', 'Beaverton, OR', 75000, 11),
(12, 'Johnson & Johnson', 'Healthcare', 'New Brunswick, NJ', 153000, 12),
(13, 'Procter & Gamble', 'Consumer Goods', 'Cincinnati, OH', 99200, 13),
(14, 'ExxonMobil', 'Energy', 'Irving, TX', 71000, 14),
(15, 'Chevron', 'Energy', 'San Ramon, CA', 48000, 15),
(16, 'Ford', 'Automotive', 'Dearborn, MI', 186000, 16),
(17, 'General Motors', 'Automotive', 'Detroit, MI', 155000, 17),
(18, 'IBM', 'Tech', 'Armonk, NY', 350000, 18),
(19, 'Oracle', 'Software', 'Redwood City, CA', 132000, 19),
(20, 'AT&T', 'Retail', 'Dallas, TX', 230000, 20),
(21, 'Verizon', 'Retail', 'New York, NY', 135000, 21),
(22, 'Adobe', 'Software', 'San Jose, CA', 23000, 22),
(23, 'Starbucks', 'Retail', 'Seattle, WA', 35000, 23),
(24, 'McDonalds', 'Restaurants', 'Chicago, IL', 200000, 24),
(25, 'Visa', 'Financial Services', 'Foster City, CA', 19500, 25),
(26, 'Mastercard', 'Financial Services', 'Purchase, NY', 24000, 26),
(27, 'Delta Air Lines', 'Aviation', 'Atlanta, GA', 75000, 27),
(28, 'United Airlines', 'Aviation', 'Chicago, IL', 90000, 28),
(29, 'American Airlines', 'Aviation', 'Fort Worth, TX', 133700, 29),
(30, 'Boeing', 'Aerospace', 'Chicago, IL', 141000, 30),
(31, 'Wayfair', 'Furniture', 'Boston', 10000, 30),
(32, 'Toast', 'Technology', 'Boston', 4500, 2),
(33, 'PwC', 'Accounting', 'New York', 327000, 5),  
(34, 'Deloitte', 'Accounting', 'London', 415000, 5),
(35, 'Ernst & Young (EY)', 'Accounting', 'New York', 312250, 4), 
(36, 'KPMG', 'Accounting', 'Amsterdam', 265000, 4),  
(37, 'Goldman Sachs', 'Finance', 'New York', 44000, 5),  
(38, 'JPMorgan Chase', 'Finance', 'New York', 293000, 5),  
(39, 'Morgan Stanley', 'Finance', 'New York', 82000, 4),  
(40, 'BlackRock', 'Finance', 'New York', 19200, 5);

# Insert empolyees
INSERT INTO employees (EmployeeID, FirstName, LastName, JobTitle, ProfileDetails, Phone, Email, Degree, ContactManager, ProfileManager, Company) VALUES
(1, 'John', 'Doe', 'Software Engineer', 'Experienced in web development', '123-456-7890', 'johndoe@apple.com', 'Computer Science', 1, 1, 1),
(2, 'Jane', 'Smith', 'Marketing Manager', 'Expert in digital marketing and strategy', '123-456-7891', 'janesmith@apple.com', 'Business Administration', 2, 2, 1),
(3, 'David', 'Johnson', 'Software Engineer', 'Specializes in managing large tech projects', '123-456-7892', 'davidjohnson@microsoft.com', 'MBA', 3, 3, 2),
(4, 'Emily', 'Brown', 'Sales Lead', 'Expert in retail and online sales strategies', '123-456-7893', 'emilybrown@microsoft.com', 'Marketing', 4, 4, 2),
(5, 'Michael', 'Davis', 'Data Analyst', 'Specializes in data analysis and insights', '123-456-7894', 'michaeldavis@amazon.com', 'Data Science', 5, 5, 3),
(6, 'Sarah', 'Miller', 'HR Manager', 'Skilled in employee relations and recruitment', '123-456-7895', 'sarahmiller@amazon.com', 'Human Resources', 6, 6, 3),
(7, 'Robert', 'Wilson', 'Engineer', 'Works on cutting-edge automotive technologies', '123-456-7896', 'robertwilson@tesla.com', 'Mechanical Engineering', 7, 7, 4),
(8, 'Laura', 'Moore', 'Hiring Manager', 'Leads Teslas logistics and manufacturing teams', '123-456-7897', 'lauramoore@tesla.com', 'Operations Management', 8, 8, 4),
(9, 'James', 'Taylor', 'Web Developer', 'Experienced in web development for tech companies', '123-456-7898', 'jamestaylor@google.com', 'Computer Science', 9, 9, 5),
(10, 'Patricia', 'Anderson', 'UX Designer', 'Works on designing intuitive user interfaces', '123-456-7899', 'patriciaanderson@google.com', 'Graphic Design', 10, 10, 5),
(11, 'Christopher', 'Thomas', 'Product Manager', 'Manages product development for social media apps', '123-456-7900', 'christopherthomas@facebook.com', 'Business Administration', 11, 11, 6),
(12, 'Jessica', 'Jackson', 'Content Strategist', 'Creates content strategies for brand growth', '123-456-7901', 'jessicajackson@facebook.com', 'Communications', 12, 12, 6),
(13, 'William', 'White', 'Operations Analyst', 'Analyzes operations for beverage production', '123-456-7902', 'williamwhite@coca-cola.com', 'Operations Management', 13, 13, 7),
(14, 'Elizabeth', 'Harris', 'Brand Manager', 'Oversees brand strategy and consumer marketing', '123-456-7903', 'elizabethharris@coca-cola.com', 'Marketing', 14, 14, 7),
(15, 'Daniel', 'Martin', 'Supply Chain Manager', 'Manages supply chain operations in the beverage industry', '123-456-7904', 'danielmartin@pepsico.com', 'Supply Chain Management', 15, 15, 8),
(16, 'Olivia', 'Clark', 'Finance Manager', 'Manages financial operations for global markets', '123-456-7905', 'oliviaclark@pepsico.com', 'Finance', 16, 16, 8),
(17, 'Ethan', 'Lewis', 'Retail Sales Associate', 'Customer service and sales in retail stores', '123-456-7906', 'ethanlewis@walmart.com', 'Retail Management', 17, 17, 9),
(18, 'Sophia', 'Walker', 'Logistics Coordinator', 'Handles shipping and distribution of products', '123-456-7907', 'sophiawalker@walmart.com', 'Logistics', 18, 18, 9),
(19, 'Alexander', 'Young', 'Embedded Systems Engineer', 'Designs embedded systems for semiconductors', '123-456-7908', 'alexanderyoung@intel.com', 'Electrical Engineering', 19, 19, 10),
(20, 'Amelia', 'Allen', 'Product Development Lead', 'Leads product development teams in tech industry', '123-456-7909', 'ameliaallen@intel.com', 'Product Management', 20, 20, 10),
(21, 'Benjamin', 'King', 'Retail Marketing Manager', 'Develops marketing strategies for global apparel brand', '123-456-7910', 'benjaminking@nike.com', 'Marketing', 21, 21, 11),
(22, 'Mia', 'Scott', 'Footwear Product Manager', 'Manages product lines in the footwear division', '123-456-7911', 'miascott@nike.com', 'Product Management', 22, 22, 11),
(23, 'Aiden', 'Adams', 'Senior Research Scientist', 'Leads healthcare research and product innovation', '123-456-7912', 'aidenadams@johnsonandjohnson.com', 'Biomedical Engineering', 23, 23, 12),
(24, 'Isabella', 'Baker', 'Brand Communications Manager', 'Handles brand messaging and media relations', '123-456-7913', 'isabellabaker@johnsonandjohnson.com', 'Public Relations', 24, 24, 12),
(25, 'Matthew', 'Gonzalez', 'R&D Manager', 'Leads research in consumer goods innovation', '123-456-7914', 'matthewgonzalez@pg.com', 'Research & Development', 25, 25, 13),
(26, 'Charlotte', 'Nelson', 'Product Development Manager', 'Oversees consumer goods product development', '123-456-7915', 'charlottenelson@pg.com', 'Product Development', 26, 26, 13),
(27, 'Henry', 'Carter', 'Energy Analyst', 'Analyzes energy trends and market data', '123-456-7916', 'henrycarter@exxonmobil.com', 'Energy Management', 27, 27, 14),
(28, 'Zoe', 'Mitchell', 'Supply Chain Specialist', 'Works on global supply chain for energy products', '123-456-7917', 'zoemitchell@exxonmobil.com', 'Supply Chain', 28, 28, 14),
(29, 'Jack', 'Perez', 'Financial Analyst', 'Conducts financial analysis for energy sector', '123-456-7918', 'jackperez@chevron.com', 'Finance', 29, 29, 15),
(30, 'Ava', 'Roberts', 'Geologist', 'Explores geological data for energy resources', '123-456-7919', 'avaroerts@chevron.com', 'Geology', 30, 30, 15),
(31, 'Lucas', 'Turner', 'Electrical Engineer', 'Works on automotive electronics and EV technologies', '123-456-7920', 'lucasturner@ford.com', 'Electrical Engineering', 31, 31, 16),
(32, 'Mason', 'Collins', 'Manufacturing Engineer', 'Optimizes manufacturing processes in automotive', '123-456-7921', 'masoncollins@ford.com', 'Industrial Engineering', 32, 32, 16),
(33, 'Liam', 'Evans', 'Automotive Designer', 'Designs cutting-edge car models', '123-456-7922', 'liamevans@gm.com', 'Automotive Engineering', 33, 33, 17),
(34, 'Harper', 'Martin', 'Production Manager', 'Leads production teams in automotive manufacturing', '123-456-7923', 'harpermartin@gm.com', 'Operations', 34, 34, 17),
(35, 'Ella', 'Robinson', 'Software Developer', 'Develops enterprise software for tech clients', '123-456-7924', 'ellarobinson@ibm.com', 'Computer Science', 35, 35, 18),
(36, 'Jacob', 'Wright', 'Data Scientist', 'Analyzes data for technology applications', '123-456-7925', 'jacobwright@ibm.com', 'Data Science', 36, 36, 18),
(37, 'Oliver', 'Lopez', 'Cloud Solutions Architect', 'Designs cloud computing solutions for enterprises', '123-456-7926', 'oliverlopez@oracle.com', 'Information Technology', 37, 37, 19),
(39, 'Alex', 'Rivera', 'Hiring Manager', 'I am the Hiring Manager for Wayfairs Northeastern Co-ops', '(555) 392-1684', 'arivera@wayfair.com','Communications', 5, 1, 31),
(38, 'Elijah', 'Hill', 'Hiring Manager', 'Provides insights using business intelligence tools', '123-456-7927', 'elijahhill@oracle.com', 'Business Intelligence', 38, 38, 19),
(40, 'Mila', 'Gonzalez', 'Hiring Manager', 'Focuses on customer retention and satisfaction', '123-456-7929', 'milagonzalez@att.com', 'Business Administration', 40, 40, 20),
(41, 'Benjamin', 'Young', 'Cybersecurity Specialist', 'Works on securing enterprise networks and systems', '123-456-7930', 'benjaminyoung@cisco.com', 'Cybersecurity', 41, 41, 21),
(42, 'Lily', 'King', 'Network Engineer', 'Designs and maintains network infrastructure', '123-456-7931', 'lilyking@cisco.com', 'Information Technology', 42, 42, 21),
(43, 'Samuel', 'Lee', 'AI Researcher', 'Conducts research in artificial intelligence technologies', '123-456-7932', 'samuellee@openai.com', 'Artificial Intelligence', 43, 43, 22),
(44, 'Chloe', 'Martinez', 'Software Engineer', 'Designs AI-powered products and solutions', '123-456-7933', 'chloemartinez@openai.com', 'Engineering', 44, 44, 22),
(45, 'Michael', 'Hernandez', 'Software Engineer', 'Develops software for cloud-based applications', '123-456-7934', 'michaelhernandez@amazon.com', 'Computer Science', 45, 45, 3),
(46, 'Grace', 'Jackson', 'Software Engineer', 'Leads marketing efforts for tech products', '123-456-7935', 'gracejackson@amazon.com', 'Marketing', 46, 46, 3),
(47, 'Daniel', 'Wilson', 'Hiring Manager', 'Oversees technological innovations for a major startup', '123-456-7936', 'danielwilson@wayfair.com', 'Technology Management', 47, 47, 31),
(48, 'Evelyn', 'Perez', 'Operations Manager', 'Manages operations for a growing tech company', '123-456-7937', 'evelynperez@wayfair.com', 'Operations Management', 48, 48, 31),
(49, 'Henry', 'Thompson', 'Chief Financial Officer', 'Handles financial strategies for a tech company', '123-456-7938', 'henrythompson@wayfair.com', 'Finance', 49, 49, 31),
(50, 'Abigail', 'White', 'Software Engineer', 'Leads the human resources department for a major corporation', '123-456-7939', 'abigailwhite@wayfair.com', 'Human Resources', 50, 50, 31),
(51, 'Ethan', 'Taylor', 'Senior Software Developer', "Designs and implements scalable solutions for Toast's point-of-sale systems", '555-892-3471', 'ethantaylor@toast.com', 'Engineering', 51, 3, 32),
(52, 'Sophia', 'Garcia', 'Financial Analyst', "Provides data-driven insights for Amazon's financial planning and forecasting", '555-234-6789', 'sophiagarcia@amazon.com', 'Accounting & Finance', 6, 4, 3),
(53, 'Liam', 'Brown', 'Accounting Manager', "Oversees Tesla's global accounting operations and ensures compliance with financial regulations", '555-874-1234', 'liambrown@tesla.com', 'Accounting & Finance', 6, 5, 4),
(54, 'Olivia', 'Davis', 'Budget Analyst', "Manages Walmart's departmental budgets and provides expenditure insights", '555-482-9472', 'oliviadavis@walmart.com', 'Accounting & Finance', 18, 3, 9),
(55, 'James', 'Wilson', 'Tax Specialist', "Handles Nike's corporate tax filings and develops tax-saving strategies", '555-612-5487', 'jameswilson@nike.com', 'Accounting & Finance', 22, 6, 11),
(56, 'Emma', 'Martinez', 'Investment Analyst', "Advises Johnson & Johnson on portfolio management and investment opportunities", '555-329-8741', 'emmamartinez@jnj.com', 'Accounting & Finance', 24, 7, 12),
(57, 'Noah', 'Taylor', 'Cost Accountant', "Monitors cost efficiency for Procter & Gamble's manufacturing operations", '555-768-2314', 'noahtaylor@pg.com', 'Accounting & Finance', 25, 8, 13),
(58, 'Isabella', 'Moore', 'Corporate Treasurer', "Manages PepsiCo's cash flow and liquidity strategies", '555-438-5623', 'isabellamoore@pepsico.com', 'Accounting & Finance', 16, 10, 8),
(59, 'Benjamin', 'Lee', 'Accounts Payable Specialist', "Ensures Chevron's vendor payments are processed accurately and on time", '555-908-4521', 'benjaminlee@chevron.com', 'Accounting & Finance', 29, 2, 15),
(60, 'Megan', 'Harris', 'Hiring Manager', 'Oversees recruitment processes for PwC to ensure top talent acquisition.', '555-456-7890', 'megan.harris@pwc.com', 'Human Resources', 60, 27, 33),
(61, 'Ryan', 'Clark', 'Hiring Manager', 'Leads talent acquisition efforts for Deloitte, focusing on global expansion.', '555-874-3257', 'ryan.clark@deloitte.com', 'Human Resources', 61, 28, 34),
(62, 'Sophia', 'Brooks', 'Hiring Manager', 'Manages recruitment strategies for EY, specializing in senior-level positions.', '555-482-1964', 'sophia.brooks@ey.com', 'Human Resources', 62, 29, 35),
(63, 'Ethan', 'Nguyen', 'Hiring Manager', 'Drives recruitment campaigns for KPMG to support international hiring.', '555-329-8745', 'ethan.nguyen@kpmg.com', 'Human Resources', 63, 30, 36),
(64, 'Olivia', 'Parker', 'Hiring Manager', 'Focuses on identifying top financial talent for Goldman Sachs.', '555-612-3849', 'olivia.parker@goldmansachs.com', 'Human Resources', 64, 31, 37),
(65, 'James', 'Taylor', 'Hiring Manager', 'Directs recruitment for JPMorgan Chase, emphasizing diversity and inclusion.', '555-768-1423', 'james.taylor@jpmorganchase.com', 'Human Resources', 65, 32, 38),
(66, 'Liam', 'Rodriguez', 'Hiring Manager', 'Leads Morgan Stanley’s talent acquisition team to find specialized finance professionals.', '555-438-5629', 'liam.rodriguez@morganstanley.com', 'Human Resources', 66, 33, 39),
(67, 'Emma', 'Walker', 'Hiring Manager', 'Coordinates recruitment for BlackRock, focusing on investment management experts.', '555-908-4527', 'emma.walker@blackrock.com', 'Human Resources', 67, 34, 40);


# Insert Employee TAGS
INSERT INTO employee_tags (TagID, TagName, TagOwner, TaggedUser) VALUES
(1, 'Applied', 1, 1),
(2, 'Tech Genius', 2, 2),
(3, 'Problem Solver', 3, 3),
(4, 'Team Player', 4, 4),
(5, 'Quick Learner', 5, 5),
(6, 'Organized', 6, 6),
(7, 'Excellent Communicator', 7, 7),
(8, 'Hardworking', 8, 8),
(9, 'Tech Innovator', 9, 9),
(10, 'Collaborative', 10, 10),
(11, 'Creative Thinker', 11, 11),
(12, 'Innovative', 12, 12),
(13, 'Goal-Oriented', 13, 13),
(14, 'Analytical', 14, 14),
(15, 'Proactive', 15, 15),
(16, 'Applied', 16, 16),
(17, 'Tech Genius', 17, 17),
(18, 'Problem Solver', 18, 18),
(19, 'Team Player', 19, 19),
(20, 'Quick Learner', 20, 20),
(21, 'Organized', 21, 21),
(22, 'Excellent Communicator', 22, 22),
(23, 'Hardworking', 23, 23),
(24, 'Tech Innovator', 24, 24),
(25, 'Collaborative', 25, 25),
(26, 'Creative Thinker', 26, 26),
(27, 'Innovative', 27, 27),
(28, 'Goal-Oriented', 28, 28),
(29, 'Analytical', 29, 29),
(30, 'Proactive', 30, 30),
(31, 'Applied', 31, 31),
(32, 'Tech Genius', 32, 32),
(33, 'Problem Solver', 33, 33),
(34, 'Team Player', 34, 34),
(35, 'Quick Learner', 35, 35),
(36, 'Organized', 36, 36),
(37, 'Excellent Communicator', 37, 37),
(38, 'Hardworking', 38, 38),
(39, 'Tech Innovator', 39, 39),
(40, 'Collaborative', 40, 40),
(41, 'Creative Thinker', 41, 41),
(42, 'Innovative', 42, 42),
(43, 'Goal-Oriented', 43, 43),
(44, 'Analytical', 44, 44),
(45, 'Proactive', 45, 45),
(46, 'Applied', 46, 46),
(47, 'Tech Genius', 47, 47),
(48, 'Problem Solver', 48, 48),
(49, 'Team Player', 49, 49),
(50, 'Quick Learner', 50, 50),
(51, 'Looking for Co-op', 67, 29),
(52, 'Looking for Co-op', 67, 40),
(53, 'Looking for Co-op', 67, 47),
(54, 'Looking for Co-op', 67, 5),
(55, 'Looking for Co-op', 67, 41),
(56, 'Looking for Co-op', 67, 50),
(57, 'Looking for Co-op', 67, 18),
(58, 'Looking for Co-op', 67, 19),
(59, 'Looking for Co-op', 67, 27),
(60, 'Looking for Co-op', 67, 9),
(61, 'Looking for Co-op', 67, 31),
(62, 'Looking for Co-op', 67, 32),
(63, 'Looking for Co-op', 67, 14),
(64, 'Looking for Co-op', 67, 37);

# Insert TAGS STUDENT TAGS
INSERT INTO student_tags (TagID, TagName, TagOwner, TaggedUser) VALUES
(1, 'Applied', 1, 1),
(2, 'Alumni', 2, 2),
(3, 'Alumni', 3, 3),
(4, 'Quick Learner', 4, 4),
(5, 'Team Player', 5, 5),
(6, 'Organized', 6, 6),
(7, 'Tech Innovator', 7, 7),
(8, 'Collaborative', 8, 8),
(9, 'Creative Thinker', 9, 9),
(10, 'Innovative', 10, 10),
(11, 'Goal-Oriented', 11, 11),
(12, 'Hardworking', 12, 12),
(13, 'Proactive', 13, 13),
(14, 'Analytical', 14, 14),
(15, 'Tech Genius', 15, 15),
(16, 'Applied', 16, 16),
(17, 'Quick Learner', 17, 17),
(18, 'Tech Innovator', 18, 18),
(19, 'Creative Thinker', 19, 19),
(20, 'Alumni', 20, 20),
(21, 'Alumni', 21, 21),
(22, 'Alumni', 22, 22),
(23, 'Problem Solver', 23, 23),
(24, 'Collaborative', 24, 24),
(25, 'Goal-Oriented', 25, 25),
(26, 'Tech Genius', 26, 26),
(27, 'Hardworking', 27, 27),
(28, 'Team Player', 28, 28),
(29, 'Creative Thinker', 29, 29),
(30, 'Quick Learner', 30, 30),
(31, 'Innovative', 31, 31),
(32, 'Organized', 32, 32),
(33, 'Proactive', 33, 33),
(34, 'Applied', 34, 34),
(35, 'Tech Innovator', 35, 35),
(36, 'Goal-Oriented', 36, 36),
(37, 'Problem Solver', 37, 37),
(38, 'Collaborative', 38, 38),
(39, 'Analytical', 39, 39),
(40, 'Creative Thinker', 40, 40),
(41, 'Innovative', 41, 41),
(42, 'Alumni', 42, 42),
(43, 'Hardworking', 43, 43),
(44, 'Proactive', 44, 44),
(45, 'Goal-Oriented', 45, 45),
(46, 'Tech Genius', 46, 46),
(47, 'Quick Learner', 47, 47),
(48, 'Organized', 48, 48),
(49, 'Creative Thinker', 49, 49),
(50, 'Tech Innovator', 50, 50),
(51, 'Alumni',56, 1),
(52, 'Alumni',56, 2),
(53, 'Alumni',56, 9),
(54, 'Alumni',56, 10),
(55, 'Alumni',56, 11),
(56, 'Alumni',56, 12),
(57, 'Alumni',56, 35),
(58, 'Alumni',56, 36),
(59, 'Alumni',56, 4),
(60, 'Alumni',56, 45),
(61, 'Alumni',49, 16),
(62, 'Alumni',49, 29),
(63, 'Alumni',49, 49),
(64, 'Alumni',49, 52),
(65, 'Alumni',49, 53),
(66, 'Alumni',49, 54),
(67, 'Alumni',49, 55),
(68, 'Alumni',49, 62),
(69, 'Alumni',49, 64),
(70, 'Alumni',49, 67);

# Insert POSITIONS CO-Op
INSERT INTO internships (PositionID, JobTitle, StartDate, EndDate, Company, PositionHolder, Supervisor) VALUES
(1, 'Lead Coder', '2023-01-10', '2023-07-10', 1, 1, 12),
(2, 'Creative Designer', '2023-02-15', '2023-08-15', 2, 25, 4),
(3, 'Marketing Specialist', '2023-03-20', '2023-09-20', 3, 40, 10),
(4, 'Data Analyst', '2023-04-05', '2023-10-05', 4, 19, 2),
(5, 'Software Engineer', '2023-05-01', '2023-11-01', 5, 7, 18),
(6, 'Product Manager', '2023-06-10', '2023-12-10', 6, 3, 20),
(7, 'Business Analyst', '2023-07-05', '2023-01-05', 7, 21, 11),
(8, 'UX Researcher', '2023-08-15', '2024-02-15', 8, 14, 24),
(9, 'Financial Analyst', '2023-09-10', '2024-03-10', 9, 8, 22),
(10, 'Operations Intern', '2023-10-01', '2024-04-01', 10, 12, 29),
(11, 'HR Coordinator', '2023-11-12', '2024-05-12', 11, 6, 25),
(12, 'Brand Strategist', '2023-12-20', '2024-06-20', 12, 5, 9),
(13, 'Content Creator', '2024-01-25', '2024-07-25', 13, 13, 14),
(14, 'Data Scientist', '2024-02-15', '2024-08-15', 14, 17, 3),
(15, 'Data Scientist', '2024-03-05', '2024-09-05', 15, 50, 8),
(16, 'Digital Marketer', '2024-04-10', '2024-10-10', 16, 33, 21),
(17, 'Sales Intern', '2024-05-20', '2024-11-20', 17, 18, 7),
(18, 'Data Scientist', '2024-06-01', '2024-12-01', 18, 30, 6),
(19, 'Software Engineer', '2024-07-15', '2025-01-15', 19, 9, 15),
(20, 'Project Manager', '2024-08-10', '2025-02-10', 20, 31, 4),
(21, 'Data Scientist', '2024-09-05', '2025-03-05', 21, 26, 13),
(22, 'Data Scientist', '2024-10-20', '2025-04-20', 22, 11, 17),
(23, 'Operations Assistant', '2024-11-25', '2025-05-25', 23, 1, 16),
(24, 'Supply Chain Analyst', '2024-12-15', '2025-06-15', 24, 41, 32),
(25, 'Creative Writer', '2025-01-10', '2025-07-10', 25, 42, 5),
(26, 'Network Administrator', '2025-02-20', '2025-08-20', 26, 8, 1),
(27, 'Financial Planning Intern', '2025-03-05', '2025-09-05', 27, 16, 11),
(28, 'Software Engineer', '2025-04-01', '2025-10-01', 28, 13, 23),
(29, 'Research Assistant', '2025-05-15', '2025-11-15', 29, 24, 29),
(30, 'Engineering Intern', '2025-06-01', '2025-12-01', 30, 50, 3),
(31, 'Research Assistant', '2025-07-10', '2026-01-10', 9, 5, 4),
(32, 'Community Outreach Intern', '2025-08-05', '2026-02-05', 30, 22, 19),
(33, 'Database Administrator', '2025-09-15', '2026-03-15', 31, 36, 12),
(34, 'Software Engineer', '2025-10-20', '2026-04-20', 31, 1, 30),
(35, 'Marketing Analyst', '2025-11-25', '2026-05-25', 31, 11, 5),
(36, 'Product Design Intern', '2025-12-10', '2026-06-10', 5, 38, 6),
(37, 'Research Assistant', '2026-01-05', '2026-07-05', 4, 2, 22),
(38, 'Research Assistant', '2026-02-15', '2026-08-15', 3, 27, 18),
(39, 'Software Engineer', '2026-03-25', '2026-09-25', 2, 10, 13),
(40, 'Research Assistant', '2026-04-10', '2026-10-10', 1, 3, 4),
(41, 'Software Engineer', '2023-04-13', '2023-10-15', 1, 51, 1),
(42, 'Software Engineer', '2024-04-13', '2024-10-15', 1, 52, 1),
(43, 'Software Engineer', '2023-08-13', '2024-02-15', 6, 53, 12),
(44, 'Software Engineer', '2023-01-13', '2023-06-15', 6, 54, 12),
(45, 'Software Engineer', '2023-03-13', '2023-09-15', 5, 55, 9),
(46, 'Software Engineer', '2022-04-13', '2022-10-15', 5, 56, 9),
(47, 'Software Development', '2023-04-13', '2023-10-15', 32, 13, 51),
(48, 'Software Development', '2024-04-13', '2024-10-15', 32, 21, 51),
(49, 'Software Development', '2023-08-13', '2024-02-15', 32, 36, 51),
(50, 'Software Development', '2023-01-13', '2023-06-15', 32, 32, 51),
(51, 'Software Development', '2023-03-13', '2023-09-15', 32, 35, 51),
(52, 'Software Development', '2022-04-13', '2022-10-15', 32, 54, 51);