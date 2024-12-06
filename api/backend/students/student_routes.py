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

    query = '''SELECT CONCAT(s.FirstName, ' ', s.LastName) AS 'Name', 
                      s.ExpectedGrad AS 'Grad Year', 
                      s.Major, 
                      s.Email
               FROM students AS s
               ORDER BY s.LastName'''
    
    cursor.execute(query)
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# returns student(s) with given first name name
@students.route('/students/<studentFirstName>', methods=['GET'])
def get_students_by_name(studentFirstName):
    cursor = db.get_db().cursor()
    
    query = '''SELECT CONCAT(s.FirstName, ' ', s.LastName) AS 'Name',
                      s.ExpectedGrad AS 'Grad Year', 
                      s.Major, 
                      s.Email
               FROM students AS s
               WHERE s.FirstName = %s
               ORDER BY s.LastName
            '''
    cursor.execute(query, (studentFirstName,))
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status = 200
    return the_response


# Delete a student based on their name and ID
@students.route('/students/<int:studentID>/<studentFirstName>', methods=['DELETE'])
def delete_student(studentID, studentFirstName):
    cursor = db.get_db().cursor()

    # SQL query to delete the student based on their ID and first name
    query = '''DELETE FROM students 
               WHERE StudentID = %s AND FirstName = %s'''
    try:
        cursor.execute(query, (studentID, studentFirstName))
        db.get_db().commit()

        # Check if any rows were affected (i.e., if the student was found and deleted)
        if cursor.rowcount == 0:
            return jsonify({"message": "Student not found or deletion failed"}), 404

        return jsonify({"message": "Student deleted successfully!"}), 200

    except Exception as e:
        current_app.logger.error(f"Error deleting student: {e}")
        return jsonify({"error": f"An error occurred: {e}"}), 500
    

    # Add a new student
@students.route('/students', methods=['POST'])
def add_student():
    # Get data from the request
    data = request.get_json()

    # Ensure all required fields are provided
    required_fields = ['FirstName', 'LastName', 'Major', 'Minor', 'ExpectedGrad', 'Year', 
                       'ProfileDetails', 'Phone', 'Email', 'ProfileManager']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        cursor = db.get_db().cursor()

        # Insert the new student
        query = '''INSERT INTO students (FirstName, LastName, Major, Minor, ExpectedGrad, Year, 
                                         ProfileDetails, Phone, Email, ProfileManager)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        cursor.execute(query, (data['FirstName'], data['LastName'], data['Major'], data['Minor'], 
                               data['ExpectedGrad'], data['Year'], data['ProfileDetails'], 
                               data['Phone'], data['Email'], data['ProfileManager']))

        db.get_db().commit()
        return jsonify({"message": "Student added successfully!"}), 201

    except Exception as e:
        current_app.logger.error(f"Error adding student: {e}")
        return jsonify({"error": f"An error occurred: {e}"}), 500


# Update an existing student
@students.route('/students/<int:studentID>', methods=['PUT'])
def update_student(studentID):
    # Get data from the request
    data = request.get_json()

    # Ensure at least one field is provided for update
    if not data:
        return jsonify({"error": "No data provided for update"}), 400

    # Build the update query dynamically
    update_fields = []
    query_params = []
    for key, value in data.items():
        if key in ['FirstName', 'LastName', 'Major', 'Minor', 'ExpectedGrad', 'Year', 
                   'ProfileDetails', 'Phone', 'Email', 'ProfileManager']:
            update_fields.append(f"{key} = %s")
            query_params.append(value)

    if not update_fields:
        return jsonify({"error": "No valid fields provided for update"}), 400

    query_params.append(studentID)  # Append the student ID for the WHERE clause

    try:
        cursor = db.get_db().cursor()

        # Execute the update query
        query = f"UPDATE students SET {', '.join(update_fields)} WHERE StudentID = %s"
        cursor.execute(query, query_params)
        db.get_db().commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Student not found or no changes made"}), 404

        return jsonify({"message": "Student updated successfully!"}), 200

    except Exception as e:
        current_app.logger.error(f"Error updating student: {e}")
        return jsonify({"error": f"An error occurred: {e}"}), 500
