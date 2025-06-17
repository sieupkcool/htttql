from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService
from flask import session

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({'message': 'Missing required fields'}), 400

    user = auth_service.register_user(username, password, email)
    if user:
        return jsonify({'message': 'User registered successfully'}), 201
    return jsonify({'message': 'User registration failed'}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    user = auth_service.login_user(username, password)
    if user:
        session['user_id'] = user.userid
        session['role'] = user.vitri
        session['hovaten'] = user.hovaten
        return jsonify({
            'user_id': user.userid,
            'role': user.vitri,
            'hovaten': user.hovaten
        }), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # Logic for logging out the user (e.g., invalidating the token)
    return jsonify({'message': 'User logged out successfully'}), 200