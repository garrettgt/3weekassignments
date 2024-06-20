from flask import Flask, jsonify

app = Flask(__name__)

students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/old_students', methods=['GET'])
def get_old_students():
    old_students_ar = []
    for idx in students:
        if int(idx['age']) > 20:
            old_students_ar.append(idx)
    return old_students_ar

@app.route('/young_students', methods=['GET'])
def get_young_students():
    young_students_ar = []
    for idx in students:
        if int(idx['age']) < 21:
            young_students_ar.append(idx)
    return young_students_ar

@app.route('/advance_students', methods=['GET'])
def get_advance_students():
    advance_students_ar = []
    for idx in students:
        if int(idx['age'] < 21 and idx['grade'] == 'A'):
            advance_students_ar.append(idx)
    return advance_students_ar

@app.route('/student_names', methods=['GET'])
def get_student_names():
    student_names_ar = []
    for idx in students:
        student_names_ar.append({'first_name' : idx['first_name'], 'last_name' : idx['last_name']})
    return student_names_ar

@app.route('/student_ages', methods=['GET'])
def get_student_ages():
    student_ages_ar = []
    for idx in students:
        student_ages_ar.append({'student_name' : f"{idx['first_name']} {idx['last_name']}", 'age' : idx['age']})
    return student_ages_ar

if __name__ == '__main__':
    app.run(debug=True)