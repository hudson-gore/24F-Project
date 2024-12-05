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
    

# Get a student by their ID
@students.route('/students/id/<int:studentID>', methods=['GET'])
def get_student_by_id(studentID):
    cursor = db.get_db().cursor()

    # SQL query to retrieve the student's details based on their ID
    query = '''SELECT CONCAT(s.FirstName, ' ', s.LastName) AS 'Name',
                      s.Major, 
                      s.Minor,
                      s.ExpectedGrad AS 'Grad Year', 
                      s.Year,
                      s.ProfileDetails,
                      s.Phone,
                      s.Email
               FROM students AS s
               WHERE s.StudentID = %s'''

    try:
        cursor.execute(query, (studentID,))
        theData = cursor.fetchone()

        # Check if the student exists
        if not theData:
            return jsonify({"error": "Student not found"}), 404

        # Convert the result to a dictionary for easy JSON conversion
        student_data = {
            "Name": theData[0],
            "Major": theData[1],
            "Minor": theData[2],
            "Grad Year": theData[3],
            "Year": theData[4],
            "ProfileDetails": theData[5],
            "Phone": theData[6],
            "Email": theData[7],
        }

        return jsonify(student_data), 200

    except Exception as e:
        current_app.logger.error(f"Error retrieving student: {e}")
        return jsonify({"error": f"An error occurred: {e}"}), 500