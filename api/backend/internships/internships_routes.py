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
internships = Blueprint('internships', __name__)

# Routes

# Return all of the internship experiences in the database
@internships.route('/internships', methods=['GET'])
def get_all_internships():
    cursor = db.get_db().cursor()

    query = '''SELECT *
               FROM internships
            '''
     
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status = 200
    return the_response


# Returns all of the students that have held a specific internship
# in the past and their contact info
@internships.route('/internships/<position>', methods=['GET'])
def internship_holders(position):
    cursor = db.get_db().cursor()

    query = '''SELECT s.FirstName, s.LastName, s.Year, s.Major, s.Email, s.Phone
               FROM students s
               JOIN internships i ON s.StudentID = i.PositionHolder
               WHERE i.PositionID = %s'''
    
    cursor.execute(query, (position,))
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status = 200
    return the_response

# Add a new intership experience for a specific student
@internships.route('/internships', methods=['POST'])
def internship_experience():
    
    job_data = request.json
    required_fields = ['JobTitle', 'StartDate', 'EndDate', 'Company', 'PositionHolder',
                       'Supervisor']
    if not all(field in job_data for field in required_fields):
        return "Missing required fields in the request data."
    
    title = job_data['JobTitle']
    start = job_data['StartDate']
    end = job_data['EndDate']
    company = job_data['Company']
    intern = job_data['PositionHolder']
    manager = job_data['Supervisor']

    query = '''INSERT INTO internships (JobTitle, StartDate, EndDate, Company, 
                                        PositionHolder, Supervisor)
               VALUES (%s, %s, %s, %s, %s, %s)
            '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Successfully Added Internship Experience!")
    response.status_code = 200
    return response

# Edit internship experiences for specific students existing in the system
@internships.route('/internships', methods=['PUT'])
def update_internship():
    
    current_app.logger.info('PUT /internships route')

    intern_info = request.json
    required_fields = ['JobTitle', 'StartDate', 'EndDate', 'Company', 'PositionHolder',
                       'Supervisor']
    if not all(field in intern_info for field in required_fields):
        return "Missing required fields in the request data."
    
    title = intern_info['JobTitle']
    start = intern_info['StartDate']
    end = intern_info['EndDate']
    company = intern_info['Company']
    intern = intern_info['PositionHolder']
    manager = intern_info['Supervisor']
    id = intern_info['PositionID']

    query = '''UPDATE internships
               SET JobTitle = %s, StartDate = %s, EndDate = %s, Company = %s,
                   PositionHolder = %s, Supervisor = %s
               WHERE PositionID = %s
            '''
    data = (title, start, end, company, intern, manager, id)

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    
    return "Contact info updated successfully!"

# Delete a specific internship role from the system
@internships.route('/internships/<position>', methods=['DELETE'])
def delete_internship(position):

    query = '''DELETE FROM internships WHERE PositionID = %s'''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return "Internship deleted successfully!"