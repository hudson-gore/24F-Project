# Import statements
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

# Creating new blueprint object
contacts = Blueprint('contacts', __name__)

# Routes

# Get all of the contacts from the system
@contacts.route('/contacts/<type>', methods=['GET'])
def get_contacts(type):
    # Define allowed table names 
    allowed_tables = {'employees, students'}

    # Check if request is valid
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
@contacts.route('/contacts/<position>/<industry>', methods=['GET'])
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
@contacts.route('/contacts/<industry>/<tag>', methods=['GET'])
def get_contacts_ind_tag(industry, tag):
    cursor = db.get_db().cursor()
    
    query = '''SELECT e.FirstName, e.LastName, e.Phone, e.Email 
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
@contacts.route('contacts/<company>/<position>', methods=['GET'])
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
@contacts.route('/contacts/<industry>/<size>/<tag>', methods=['GET'])
def get_contacts_ind_sz_tag(industry, size, tag):
    try:
        # Validate that size is an integer
        try:
            size = int(size)
        except ValueError:
            return make_response(jsonify({"error": "Invalid company size provided"}), 400)

        cursor = db.get_db().cursor()

        # Query to get contacts
        query = '''SELECT e.FirstName, e.LastName, e.Email, e.Phone
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
    
    