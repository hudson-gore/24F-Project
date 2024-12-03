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