from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # 블루프린트
    from .views import main_views, exam_views, subjects_views, scores_views, students_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(exam_views.bp)
    app.register_blueprint(subjects_views.bp)
    app.register_blueprint(scores_views.bp)
    app.register_blueprint(students_views.bp)

    return app