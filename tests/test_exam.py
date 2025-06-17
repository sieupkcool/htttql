from flask import Flask, jsonify, request
from app import app
from app.models import Exam
from app.services.exam_service import ExamService

@app.route('/exams', methods=['GET'])
def get_exams():
    exams = ExamService.get_all_exams()
    return jsonify(exams), 200

@app.route('/exams', methods=['POST'])
def create_exam():
    data = request.get_json()
    exam = ExamService.create_exam(data)
    return jsonify(exam), 201

@app.route('/exams/<int:exam_id>', methods=['PUT'])
def update_exam(exam_id):
    data = request.get_json()
    exam = ExamService.update_exam(exam_id, data)
    return jsonify(exam), 200

@app.route('/exams/<int:exam_id>', methods=['DELETE'])
def delete_exam(exam_id):
    ExamService.delete_exam(exam_id)
    return jsonify({'message': 'Exam deleted successfully'}), 204