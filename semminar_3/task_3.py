from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    group = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    grades = db.relationship('Grade', backref='student', lazy=True)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Integer, nullable=False)

db.create_all()

@app.route('/students', methods=['GET'])
def get_students_with_grades():
    students = Student.query.all()
    student_grades = []
    for student in students:
        grades = [{'subject': grade.subject, 'grade': grade.grade} for grade in student.grades]
        student_grades.append({
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'group': student.group,
            'email': student.email,
            'grades': grades
        })
    return jsonify(student_grades)

if __name__ == '__main__':
    app.run(debug=True)
