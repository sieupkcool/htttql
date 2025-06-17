from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import nguoidung
from app import db

class AuthService:
    @staticmethod
    def register_user(username, password, email):
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = nguoidung(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def login_user(username, password):
        user = nguoidung.query.filter_by(username=username).first()
        if user and user.password == password:
            return user
        return None

    @staticmethod
    def get_user_by_id(user_id):
        return nguoidung.query.get(user_id)

    @staticmethod
    def update_user(user, username=None, email=None):
        if username:
            user.username = username
        if email:
            user.email = email
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()