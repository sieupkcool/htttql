from flask import Blueprint

# Initialize the routes blueprint
routes_bp = Blueprint('routes', __name__)

# Import all route modules to register their routes
from . import auth, user, department, subject, exam, question, assignment, statistics

# Register the blueprint with the main app in app/__init__.py