from flask import Blueprint, request, jsonify
from app.services.exam_service import ExamService

exam_bp = Blueprint('exam', __name__)
exam_service = ExamService()

@exam_bp.route('/exams', methods=['POST'])
def create_exam():
    data = request.get_json()
    print(data)  # Kiểm tra dữ liệu nhận được
    result = ExamService.create_exam(data)
    return jsonify(result), 201 if result.get("message") == "Exam created successfully" else 400

@exam_bp.route('/exams/<int:exam_id>', methods=['PUT'])
def update_exam(exam_id):
    data = request.json
    exam = exam_service.update_exam(exam_id, data)
    return jsonify(exam), 200

@exam_bp.route('/exams/<int:exam_id>', methods=['DELETE'])
def delete_exam(exam_id):
    exam_service.delete_exam(exam_id)
    return jsonify({'message': 'Exam deleted successfully'}), 204

@exam_bp.route('/exams', methods=['GET'])
def get_exams():
    exams = exam_service.get_all_exams()
    return jsonify(exams), 200

@exam_bp.route('/exams/<int:exam_id>', methods=['GET'])
def get_exam(exam_id):
    exam = exam_service.get_exam_by_id(exam_id)
    return jsonify(exam), 200