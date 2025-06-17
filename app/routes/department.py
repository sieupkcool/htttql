from flask import Blueprint, request, jsonify
from app.models import Khoa
from app.services.department_service import DepartmentService

department_bp = Blueprint('department', __name__)
department_service = DepartmentService()

@department_bp.route('/departments', methods=['POST'])
def add_department():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'message': 'Department name is required'}), 400
    department = department_service.create_department(name)
    return jsonify(department), 201

@department_bp.route('/departments/<int:department_id>', methods=['PUT'])
def update_department(department_id):
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'message': 'Department name is required'}), 400
    department = department_service.update_department(department_id, name)
    if department is None:
        return jsonify({'message': 'Department not found'}), 404
    return jsonify(department), 200

@department_bp.route('/departments/<int:department_id>', methods=['DELETE'])
def delete_department(department_id):
    success = department_service.delete_department(department_id)
    if not success:
        return jsonify({'message': 'Department not found'}), 404
    return jsonify({'message': 'Department deleted successfully'}), 200

@department_bp.route('/departments', methods=['GET'])
def get_departments():
    departments = department_service.get_all_departments()
    return jsonify(departments), 200