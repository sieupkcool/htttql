from flask import Flask
from app.models import db
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')
    db.init_app(app)

    CORS(app)

    # Import blueprints
    from app.routes.auth import auth_bp
    from app.routes.user import user_bp
    from app.routes.department import department_bp
    from app.routes.subject import subject_bp
    from app.routes.exam import exam_bp
    from app.routes.question import question_bp
    from app.routes.assignment import assignment_bp
    from app.routes.statistics import statistics_bp
    from app.routes.page import page_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(subject_bp)
    app.register_blueprint(exam_bp)
    app.register_blueprint(question_bp)
    app.register_blueprint(assignment_bp)
    app.register_blueprint(statistics_bp)
    app.register_blueprint(page_bp)

    return app

app = create_app()