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

    query = ''' SELECT * FROM {type}}'''
    cursor.execute(query)

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response