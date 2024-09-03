from flask import Blueprint, render_template, request, redirect, url_for
from exam.database import execute_query

bp = Blueprint('scores', __name__, url_prefix='/scores')

@bp.route('/')
def score_list():
    query = """
    SELECT e.exam_id, s.subjects, u.name, e.score, e.exam_date
    FROM exam e
    JOIN subjects s ON e.subject_id = s.subject_id
    JOIN user u ON e.user_id = u.user_id
    """
    scores = execute_query(query)
    return render_template('scores/score_list.html', scores=scores)

@bp.route('/create', methods=['GET', 'POST'])
def score_create():
    if request.method == 'POST':
        subject_id = request.form['subject_id']
        user_id = request.form['user_id']
        score = request.form['score']
        exam_date = request.form['exam_date']
        query = "INSERT INTO exam (subject_id, user_id, score, exam_date) VALUES (%s, %s, %s, %s)"
        execute_query(query, (subject_id, user_id, score, exam_date))
        return redirect(url_for('scores.score_list'))
    
    subjects = execute_query("SELECT * FROM subjects")
    users = execute_query("SELECT * FROM user")
    return render_template('scores/score_form.html', subjects=subjects, users=users)

@bp.route('/update/<int:exam_id>', methods=['GET', 'POST'])
def score_update(exam_id):
    if request.method == 'POST':
        subject_id = request.form['subject_id']
        user_id = request.form['user_id']
        score = request.form['score']
        exam_date = request.form['exam_date']
        query = "UPDATE exam SET subject_id = %s, user_id = %s, score = %s, exam_date = %s WHERE exam_id = %s"
        execute_query(query, (subject_id, user_id, score, exam_date, exam_id))
        return redirect(url_for('scores.score_list'))
    
    query = "SELECT * FROM exam WHERE exam_id = %s"
    score = execute_query(query, (exam_id,))[0]
    subjects = execute_query("SELECT * FROM subjects")
    users = execute_query("SELECT * FROM user")
    return render_template('scores/score_form.html', score=score, subjects=subjects, users=users)

@bp.route('/delete/<int:exam_id>')
def score_delete(exam_id):
    query = "DELETE FROM exam WHERE exam_id = %s"
    execute_query(query, (exam_id,))
    return redirect(url_for('scores.score_list'))