# Import statements
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from flask import abort
from backend.db_connection import db
from backend.ml_models.model01 import predict

# Creating new blueprint object
contacts = Blueprint('contacts', __name__)

# Routes

# Get all of the contacts from the system
@contacts.route('/contacts/<type>', methods=['GET'])
def get_contacts(type):

    allowed_tables = {'employees, students'}

    if type not in allowed_tables:
        return make_response(jsonify({"error": "Invalid type specified"}))
    
    cursor = db.get_db().cursor()

    query = ''' SELECT * FROM {type}'''
    cursor.execute(query)

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get all the contacts for a specific position and indsutry
@contacts.route('/contacts/employees/<position>/<industry>', methods=['GET'])
def get_contacts_pos_ind(position, industry):
    cursor = db.get_db().cursor()
    
    query = '''SELECT e.FirstName, e.LastName, e.Phone, e.Email 
               FROM employees e
               JOIN companies c ON e.Company = c.CompanyID
               WHERE e.JobTitle = %s AND c.Industry = %s'''
    cursor.execute(query, (position, industry))

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get all the contacts in a specifc industry with a specific tag
@contacts.route('/contacts/employees/<industry>/<tag>', methods=['GET'])
def get_contacts_ind_tag(industry, tag):
    cursor = db.get_db().cursor()
    
    query = '''SELECT e.FirstName, e.LastName, e.JobTitle, e.Phone, e.Email 
               FROM employees e
               JOIN people p ON p.ID = e.EmployeeID
               JOIN tags t ON p.ID = t.TaggedUser
               JOIN companies c ON e.Company = c.CompanyID
               WHERE c.Industry = %s AND t.TagName = %s'''
    cursor.execute(query, (industry, tag))

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get all of the students who have held a specific co-op
@contacts.route('contacts/students/<company>/<position>', methods=['GET'])
def get_contacts_spec_pos(company, position):    
    cursor = db.get_db().cursor()

    query = '''SELECT s.FirstName, s.LastName, s.Email, s.Phone
               FROM students s
               JOIN people p ON s.StudentID = p.ID
               JOIN internships i ON p.ID = i.PositionHolder
               JOIN companies c ON c.CompanyID = i.Company
               WHERE c.CompanyName = %s AND i.JobTitle = %s
               '''
    cursor.execute(query, (company, position))

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get all of the contacts of employees from a specific industry, with
# a defined company size, and specific tag
@contacts.route('/contacts/employees/<industry>/<size>/<tag>', methods=['GET'])
def get_contacts_ind_sz_tag(industry, size, tag):
    try:
        try:
            size = int(size)
        except ValueError:
            return make_response(jsonify({"error": "Invalid company size provided"}), 400)

        cursor = db.get_db().cursor()

        query = '''SELECT e.FirstName, e.LastName, e.JobTitle, e.Email, e.Phone
                   FROM employees e
                   JOIN companies c ON e.Company = c.CompanyID
                   JOIN people p ON e.EmployeeID = p.ID
                   JOIN tags t ON p.ID = t.TaggedUser
                   WHERE c.Industry = %s
                        AND c.Size <= %s
                        AND t.TagName = %s'''
        cursor.execute(query, (industry, size, tag))

        theData = cursor.fetchall()

        if not theData:
            return make_response(jsonify({"error": "No contacts found for the given criteria"}), 404)

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        # Catch all other exceptions
        return make_response(jsonify({"error": f"An error occurred: {str(e)}"}), 500)
    
# Get all of the employees who graduated with a specifc degree and 
# have a specfic tag
@contacts.route('/contacts/employees/<degree>/<tag>', methods=['GET'])
def get_contacts_deg_tag(degree, tag):
    cursor = db.get_db().cursor()

    query = '''SELECT e.FirstName, e.LastName, e.JobTitle, e.Email, e.Phone
               FROM employees e
               JOIN people p ON e.EmployeeID = p.ID
               JOIN tags t ON p.ID = t.TaggedUser
               WHERE e.Degree = %s AND t.TagName = %s'''
    cursor.execute(query, (degree, tag))

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get all of the employee contacts that have completed a specified 
# internship/co-op in the past and has the desired tag
@contacts.route('/contacts/employees/<position>/<tag>', methods=['GET'])
def get_contacts_intern_tag(position, tag):
    cursor = db.get_db().cursor()

    query = '''SELECT e.FirstName, e.LastName, e.JobTitle, e.Email, e.Phone
               FROM employees e
               JOIN people p ON p.ID = e.EmployeeID
               JOIN internships i ON p.ID = i.PositionHolder
               JOIN tags t ON p.ID = t.TaggedUser
               WHERE i.JobTitle = %s AND t.TagName = %s'''
    cursor.execute(query, (position, tag))

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get all of the students with a specific major and desired tag
@contacts.route('/contacts/students/<major>/<tag>', methods=['GET'])
def get_contacts_major_tag(major, tag):
    cursor = db.get_db().cursor()

    query = '''SELECT s.FirstName, s.LastName, s.Year, s.Email, s.Phone
               FROM students s
               JOIN people p ON s.StudentID = p.ID
               JOIN tags t ON p.ID = t.TaggedUser
               WHERE s.Major = %s AND t.TagName = %s'''
    
    cursor.execute(query, (major, tag))

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get a list of all of the students with a specifc tag
@contacts.route('/contacts/students/<tag>', methods=['GET'])
def get_contacts_taggged(tag):
    cursor = db.get_db().cursor()

    query = '''SELECT s.FirstName, s.LastName, s.Year, s.Major, s.Email, s.Phone
               FROM students s
               JOIN people p ON s.StudentID = p.ID
               JOIN tags t on p.ID = t.TaggedUser
               WHERE t.TagName = %s'''
    
    cursor.execute(query, (tag))

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get the contact info of a specific user
@contacts.route('/contact/<type>/<id>', methods=['GET'])
def get_contact_info(type, id):
    cursor = db.get_db().cursor()
        
    if type not in ['student', 'employee']:
        abort(400, description="Invalid contact type. Use 'student' or 'employee'.")

    
    queries = {
        'student': '''SELECT s.FirstName, s.LastName, s.Email, s.Phone
                        FROM students s
                        WHERE s.StudentID = %s''',
        'employee': '''SELECT e.FirstName, e.LastName, e.Email, e.Phone
                        FROM employees e
                        WHERE e.EmployeeID = %s'''
    }

    query = queries[type]
    cursor.execute(query, (id,))
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    

    if not theData:
        abort(404, description="Contact not found.")

    return the_response
    
# Add a new contact
@contacts.route('/contact/<type>', methods=['POST'])
def add_contact_info(type):
    
    if type not in ['student', 'employee']:
        return "Invalid contact type. Use 'student' or 'employee'."

    the_data = request.json
    required_fields = ['FirstName', 'LastName', 'Email', 'Phone']
    if not all(field in the_data for field in required_fields):
        return "Missing required fields in request data."

    firstname = the_data['FirstName']
    lastname = the_data['LastName']
    email = the_data['Email']
    phone = the_data['Phone']

    queries = {
        'student': '''INSERT INTO students (FirstName, LastName, Email, Phone)
                        VALUES (%s, %s, %s, %s)''',
        'employee': '''INSERT INTO employees (FirstName, LastName, Email, Phone)
                        VALUES (%s, %s, %s, %s)'''
    }
    query = queries[type]

    db_connection = db.get_db()
    cursor = db_connection.cursor()
    cursor.execute(query, (firstname, lastname, email, phone))
    db_connection.commit()


    response = make_response("Successfully added contact.")
    response.status_code = 200
    return response

# Update the info in an existing contact
@contacts.route('/contact/<type>', methods=['PUT'])
def update_contact_info(type):
  
    current_app.logger.info('PUT /contacts route')

    if type not in ['student', 'employee']:
        return "Invalid contact type. Use 'student' or 'employee'."

    contact_info = request.json
    required_fields = ['ID', 'FirstName', 'LastName', 'Email', 'Phone']
    if not all(field in contact_info for field in required_fields):
        return "Missing required fields in request data."

    contact_id = contact_info['ID']
    firstname = contact_info['FirstName']
    lastname = contact_info['LastName']
    email = contact_info['Email']
    phone = contact_info['Phone']

    queries = {
        'student': '''UPDATE students
                        SET FirstName = %s, LastName = %s, Email = %s, Phone = %s
                        WHERE StudentID = %s''',
        'employee': '''UPDATE employees
                        SET FirstName = %s, LastName = %s, Email = %s, Phone = %s
                        WHERE EmployeeID = %s'''
    }
    query = queries[type]

    db_connection = db.get_db()
    cursor = db_connection.cursor()
    cursor.execute(query, (firstname, lastname, email, phone, contact_id))
    db_connection.commit()

    return "Contact info updated successfully!"

# Delete an existing contact
@contacts.route('/contact/<type>/<id>', methods=['DELETE'])
def delete_contact(type, id):
    
    if type not in ['student', 'employee']:
        return "Invalid contact type. Use 'student' or 'employee'."

    queries = {
        'student': '''DELETE FROM students WHERE StudentID = %s''',
        'employee': '''DELETE FROM employees WHERE EmployeeID = %s'''
    }
    query = queries[type]

    db_connection = db.get_db()
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    return "Contact Deleted Successfully!"