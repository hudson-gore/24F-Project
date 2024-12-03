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