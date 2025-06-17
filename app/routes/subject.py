from flask import Blueprint, request, jsonify
from app.models import monhoc
from app.services.subject_service import SubjectService

subject_bp = Blueprint('subject', __name__)
subject_service = SubjectService()

@subject_bp.route('/subjects', methods=['POST'])
def add_subject():
    data = request.json
    subject = subject_service.create_subject(data)
    return jsonify(subject), 201

@subject_bp.route('/subjects/<int:subject_id>', methods=['PUT'])
def update_subject(subject_id):
    data = request.json
    subject = subject_service.update_subject(subject_id, data)
    return jsonify(subject), 200

@subject_bp.route('/subjects/<int:subject_id>', methods=['DELETE'])
def delete_subject(subject_id):
    subject_service.delete_subject(subject_id)
    return jsonify({'message': 'Subject deleted successfully'}), 204

@subject_bp.route('/subjects', methods=['GET'])
def get_subjects():
    subjects = subject_service.get_all_subjects()
    return jsonify(subjects), 200

@subject_bp.route('/subjects/<int:subject_id>', methods=['GET'])
def get_subject(subject_id):
    subject = subject_service.get_subject_by_id(subject_id)
    return jsonify(subject), 200