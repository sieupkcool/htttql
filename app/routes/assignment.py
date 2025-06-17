from flask import Blueprint, request, jsonify
from app.services.assignment_service import AssignmentService

assignment_bp = Blueprint('assignment', __name__)
assignment_service = AssignmentService()

@assignment_bp.route('/assignments', methods=['POST'])
def create_assignment():
    data = request.json
    try:
        assignment = assignment_service.create_assignment(data)
        return jsonify(assignment), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@assignment_bp.route('/assignments/<int:assignment_id>', methods=['GET'])
def get_assignment(assignment_id):
    try:
        assignment = assignment_service.get_assignment(assignment_id)
        return jsonify(assignment), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@assignment_bp.route('/assignments/<int:assignment_id>', methods=['PUT'])
def update_assignment(assignment_id):
    data = request.json
    try:
        updated_assignment = assignment_service.update_assignment(assignment_id, data)
        return jsonify(updated_assignment), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@assignment_bp.route('/assignments/<int:assignment_id>', methods=['DELETE'])
def delete_assignment(assignment_id):
    try:
        assignment_service.delete_assignment(assignment_id)
        return jsonify({'message': 'Assignment deleted successfully'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@assignment_bp.route('/assignments')
def get_assignments():
    giangvienid = request.args.get('giangvienid')
    # Lấy danh sách phân công cho giảng viên này
    assignments = AssignmentService.get_assignments_for_giangvien(giangvienid)
    return jsonify(assignments)