import csv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg://garrett:1234@localhost:5432/school"

db.init_app(app)

# define sqlalchemy models for the following entities:
# students
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'age' : self.age,
            'subject' : self.subject
        }

    def students_classes(self):
        return {
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'age' : self.age,
            'class' : {
                'subject' : self.subject,
                'teacher' : f"{Teachers[self.subject]['first_name']} {Teachers[self.subject]['first_name']}"
            }
        }

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))

    def to_dict(self):
        return {
            'id' : self.id,
            'subject' : self.subject
        }
    
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'age' : self.age,
            'subject' : self.subject
        }
        

# endpoints

@app.route("/")
def welcome():
    return "<h1>Welcome to the school's database</h1>"

# /students : return a list of students along w their class names and teacher

@app.route("/students", methods=['GET'])
def student_info():
    student_data = [stud.students_classes() for stud in Student.query.all()]
    print(student_data)
    return jsonify(student_data)

# /teachers returns a list of teachers, the subjects they teach, and the students within each subject

# /subjects return a list of subject dicts with the students enrolled in each class and the tacher who teaches the each subject





if __name__ == '__main__':
    app.run(debug=True)

