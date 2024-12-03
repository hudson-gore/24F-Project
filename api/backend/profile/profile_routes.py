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
profile = Blueprint('profile', __name__)

# Routes

# Return all of the student or employee profiles
@profile.route('/profile/<type>', methods=['GET'])
def get_all_profiles(type):
    
    if type not in ['student', 'employee']:
        return "Invalid contact type. Use 'student' or 'employee'."
    
    queries = {
        'student': '''SELECT *
                      FROM students
                    ''',
        'employee': '''SELECT *
                       FROM employees
                    '''
    }

    query = queries[type]
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200

    return the_response


# Return the profile for a specific user
@profile.route('/profile/<type>/<id>', methods=['GET'])
def find_profile(type, id):

    if type not in ['student', 'employee']:
        return "Invalid contact type. Use 'student' or 'employee'."
    
    queries = {
        'student': '''SELECT *
                      FROM students 
                      WHERE StudentID = %s
                    ''',
        'employee': '''SELECT *
                       FROM employees 
                       WHERE EmployeeID = %s
                    '''
    }
    query = queries[type]

    cursor = db.get_db().cursor()
    cursor.execute(query, (id,))
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200

    return the_response

# Add a profile to the database
@profile.route('/profile/<type>', methods=['POST'])
def add_profile(type):
    
    if type not in ['student', 'employee']:
        abort(400, description="Invalid contact type. Use 'student' or 'employee'.")

    profile_data = request.json

    if type == 'student':
        required_fields = ['FirstName', 'LastName', 'Major', 'ExpectedGrad', 'Year', 
                           'ProfileDetails', 'Phone', 'Email', 'ProfileManager']
        if not all(field in profile_data for field in required_fields):
            return "Missing required fields in request data."
        
        first = profile_data['FirstName']
        last = profile_data['LastName']
        major = profile_data['Major']
        grad = profile_data['ExpectedGrad']
        year = profile_data['Year']
        bio = profile_data['ProfileDetails']
        phone = profile_data['Phone']
        email = profile_data['Email']
        prof_manager = profile_data['ProfileManager']

        data = (first, last, major, grad, year, bio, phone, email, prof_manager)
        
    elif type == 'employee':
        required_fields = ['FirstName', 'LastName', 'JobTitle', 'ProfileDetails', 'Phone', 
                           'Email', 'ContactManager', 'ProfileManager', 'Company']
        if not all(field in profile_data for field in required_fields):
            return "Missing required fields in request data."
        
        first = profile_data['FirstName']
        last = profile_data['LastName']
        title = profile_data['JobTilte']
        bio = profile_data['ProfileDetails']
        phone = profile_data['Phone']
        email = profile_data['Email']
        con_manager = profile_data['ContactManager']
        prof_manager = profile_data['ProfileManager']
        company = profile_data['Company']

        data = (first, last, title, bio, phone, email, con_manager, prof_manager, company)

    queries = {
        'student': '''INSERT INTO students (FirstName, LastName, Major, ExpectedGrad, Year, 
                                             ProfileDetails, Phone, Email, ProfileManager)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''',
        'employee': '''INSERT INTO employees (FirstName, LastName, JobTile, ProfileDetails, Phone,
                                              Email, ContactManager, ProfileManager, Company)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    '''
    }

    query = queries[type]

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    response = make_response('Successfully added profile!')
    response.status_code = 200
    return response

# Edit the information of an existing profile
@profile.route('/profile/<type>', methods=['PUT'])
def update_profile(type):
    
    if type not in ['student', 'employee']:
        abort(400, description="Invalid contact type. Use 'student' or 'employee'.")

    profile_data = request.json

    if type == 'student':
        required_fields = ['FirstName', 'LastName', 'Major', 'ExpectedGrad', 'Year', 
                           'ProfileDetails', 'Phone', 'Email', 'ProfileManager', 'StudentID']
        if not all(field in profile_data for field in required_fields):
            return "Missing required fields in request data."
        
        first = profile_data['FirstName']
        last = profile_data['LastName']
        major = profile_data['Major']
        grad = profile_data['ExpectedGrad']
        year = profile_data['Year']
        bio = profile_data['ProfileDetails']
        phone = profile_data['Phone']
        email = profile_data['Email']
        prof_manager = profile_data['ProfileManager']
        id = profile_data['StudentID']

        data = (first, last, major, grad, year, bio, phone, email, prof_manager, id)
        
    elif type == 'employee':
        required_fields = ['FirstName', 'LastName', 'JobTitle', 'ProfileDetails', 'Phone', 
                           'Email', 'ContactManager', 'ProfileManager', 'Company', 'EmployeeID']
        if not all(field in profile_data for field in required_fields):
            return "Missing required fields in request data."
        
        first = profile_data['FirstName']
        last = profile_data['LastName']
        title = profile_data['JobTilte']
        bio = profile_data['ProfileDetails']
        phone = profile_data['Phone']
        email = profile_data['Email']
        con_manager = profile_data['ContactManager']
        prof_manager = profile_data['ProfileManager']
        company = profile_data['Company']
        id = profile_data['EmployeeID']

        data = (first, last, title, bio, phone, email, con_manager, prof_manager, company, id)

    queries = {
        'student': '''UPDATE students
                      SET FirstName = %s, LastName = %s, Major = %s, ExpectedGrad = %s, Year = %s,
                          ProfileDetails = %s, Phone = %s, Email = %s, ProfileManager = %s
                      WHERE EmployeeID = %s
                    ''',
        'employee': '''UPDATE employees
                       SET FirstName = %s, LastName = %s, JobTitle = %s, ProfileDetails = %s, Phone = %s, 
                           Email = %s, ContactManager = %s, ProfileManager = %s, Company = %s
                       WHERE EmployeeID = %s
                    '''
    }

    query = queries[type]

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    response = make_response('Successfully updated profile!')
    response.status_code = 200
    return response

# Delete an existing comapny profile
@profile.route('/profile/<id>', methods=['DELETE'])
def delete_profile(id):
    
    query = '''DELETE FROM companies WHERE CompanyID = %s'''
    
    cursor = db.get_db().cursor()
    cursor.execute(query, (id,))
    db.get_db().commit()

    response = make_response('Successfully deleted profile!')
    response.status_code = 200
    return response

        
    