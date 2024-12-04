# Import statements
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from flask import abort
from backend.db_connection import db

# new Blueprint object
students = Blueprint('students', __name__)

# routes

# return all students
@students.route('/students', methods=['GET'])
def get_all_students():

    cursor = db.get_db().cursor()

    query = '''SELECT s.FirstName, s.LastName, s.Major, s.Email
               FROM students AS s
               ORDER BY s.LastName'''
    
    cursor.execute(query)
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# returns student(s) with given name