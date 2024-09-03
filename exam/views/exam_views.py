from flask import Blueprint, render_template
from exam.database import execute_query

bp = Blueprint('exam', __name__, url_prefix='/exam')

@bp.route('/list')
def exam_list():
    query = """
    SELECT e.exam_id, s.subjects, u.name, e.score, e.exam_date
    FROM exam e
    JOIN subjects s ON e.subject_id = s.subject_id
    JOIN user u ON e.user_id = u.user_id
    """
    exam_list = execute_query(query)
    return render_template('exam/exam_list.html', exam_list=exam_list)

@bp.route('/pivot')
def exam_pivot():
    # 과목 목록 조회
    subjects_query = "SELECT subject_id, subjects FROM subjects"
    subjects = execute_query(subjects_query)
    
    # 피벗 테이블 데이터 조회
    pivot_query = """
    SELECT u.name,
           {}
    FROM user u
    LEFT JOIN exam e ON u.user_id = e.user_id
    LEFT JOIN subjects s ON e.subject_id = s.subject_id
    GROUP BY u.user_id, u.name
    """.format(", ".join([f"MAX(CASE WHEN s.subject_id = {subject['subject_id']} THEN e.score END) AS '{subject['subjects']}'" for subject in subjects]))
    
    pivot_data = execute_query(pivot_query)
    
    return render_template('exam/exam_pivot.html', subjects=subjects, pivot_data=pivot_data)