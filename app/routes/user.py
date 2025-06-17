from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    updated_user = UserService.update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user), 200
    return jsonify({'message': 'User not found or update failed'}), 404

@user_bp.route('/user/<int:user_id>/change-password', methods=['PATCH'])
def change_password(user_id):
    data = request.json
    success = UserService.change_user_password(user_id, data['new_password'])
    if success:
        return jsonify({'message': 'Password updated successfully'}), 200
    return jsonify({'message': 'User not found or password update failed'}), 404

@user_bp.route('/user/<int:user_id>/statistics', methods=['GET'])
def get_user_statistics(user_id):
    statistics = UserService.get_user_statistics(user_id)
    if statistics:
        return jsonify(statistics), 200
    return jsonify({'message': 'Statistics not found'}), 404