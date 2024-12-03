# Import statements
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from flask import abort
from backend.db_connection import db
from backend.students import students

# new Blueprint object
students = Blueprint('students_routes', __name__)

# routes

# return all students
@students.route('/students', methods=['GET'])
def get_all_students():

    current_app.logger.info('GET /students handler')
    response = make_response(jsonify(sample_students_data))
    response.status_code = 200
    return response

# returns student(s) with given name