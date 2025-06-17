from flask import Blueprint, request, jsonify
from app.services.question_service import QuestionService

question_bp = Blueprint('question', __name__)
question_service = QuestionService()

@question_bp.route('/questions', methods=['POST'])
def add_question():
    data = request.json
    question = question_service.add_question(data)
    return jsonify(question), 201

@question_bp.route('/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    data = request.json
    question = question_service.update_question(question_id, data)
    return jsonify(question), 200

@question_bp.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    question_service.delete_question(question_id)
    return jsonify({'message': 'Question deleted successfully'}), 204

@question_bp.route('/questions', methods=['GET'])
def get_questions():
    questions = question_service.get_all_questions()
    return jsonify(questions), 200

@question_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = question_service.get_question_by_id(question_id)
    return jsonify(question), 200