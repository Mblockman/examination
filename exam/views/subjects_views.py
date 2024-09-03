from flask import Blueprint, render_template, request, redirect, url_for
from exam.database import execute_query

bp = Blueprint('subjects', __name__, url_prefix='/subjects')

@bp.route('/')
def subject_list():
    query = "SELECT * FROM subjects"
    subjects = execute_query(query)
    return render_template('subjects/subject_list.html', subjects=subjects)

@bp.route('/create', methods=['GET', 'POST'])
def subject_create():
    if request.method == 'POST':
        subjects = request.form['subjects']
        start = request.form['start']
        end = request.form['end']
        query = "INSERT INTO subjects (subjects, start, end) VALUES (%s, %s, %s)"
        execute_query(query, (subjects, start, end))
        return redirect(url_for('subjects.subject_list'))
    return render_template('subjects/subject_form.html')

@bp.route('/update/<int:subject_id>', methods=['GET', 'POST'])
def subject_update(subject_id):
    if request.method == 'POST':
        subjects = request.form['subjects']
        start = request.form['start']
        end = request.form['end']
        query = "UPDATE subjects SET subjects = %s, start = %s, end = %s WHERE subject_id = %s"
        execute_query(query, (subjects, start, end, subject_id))
        return redirect(url_for('subjects.subject_list'))
    
    query = "SELECT * FROM subjects WHERE subject_id = %s"
    subject = execute_query(query, (subject_id,))[0]
    return render_template('subjects/subject_form.html', subject=subject)

@bp.route('/delete/<int:subject_id>')
def subject_delete(subject_id):
    query = "DELETE FROM subjects WHERE subject_id = %s"
    execute_query(query, (subject_id,))
    return redirect(url_for('subjects.subject_list'))