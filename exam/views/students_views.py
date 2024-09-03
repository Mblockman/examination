from flask import Blueprint, render_template, request, redirect, url_for
from exam.database import execute_query

bp = Blueprint('students', __name__, url_prefix='/students')

@bp.route('/')
def student_list():
    query = "SELECT * FROM user"
    students = execute_query(query)
    return render_template('students/student_list.html', students=students)

@bp.route('/create', methods=['GET', 'POST'])
def student_create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        query = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
        execute_query(query, (name, email, password))
        return redirect(url_for('students.student_list'))
    return render_template('students/student_form.html')

@bp.route('/update/<int:user_id>', methods=['GET', 'POST'])
def student_update(user_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        query = "UPDATE user SET name = %s, email = %s, password = %s WHERE user_id = %s"
        execute_query(query, (name, email, password, user_id))
        return redirect(url_for('students.student_list'))
    
    query = "SELECT * FROM user WHERE user_id = %s"
    student = execute_query(query, (user_id,))[0]
    return render_template('students/student_form.html', student=student)

@bp.route('/delete/<int:user_id>')
def student_delete(user_id):
    query = "DELETE FROM user WHERE user_id = %s"
    execute_query(query, (user_id,))
    return redirect(url_for('students.student_list'))