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
companies = Blueprint('companies', __name__)

# Routes

# Return the company profile of a specific company
@companies.route('/companies/<id>', methods=['GET'])
def get_comp_prof(id):
    cursor = db.get_db().cursor()

    query = '''SELECT *
               FROM companies
               WHERE CompanyID = %s'''
    cursor.execute(query,(id,))

    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
