from flask import Blueprint, request, jsonify
from app.services.question_service import QuestionService
from app.models import cauhoi, chitietcongviec, congviec

question_bp = Blueprint('question', __name__)
question_service = QuestionService()

@question_bp.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()
    nguoitaoid = request.headers.get('nguoitaoid')  # Lấy từ header
    phancongid = data.get('phancongid')
    data['nguoitaoid'] = nguoitaoid
    if phancongid:
        # Đếm số câu hỏi đã có
        so_cau = cauhoi.query.filter_by(phancongid=phancongid).count()
        assignment = chitietcongviec.query.get(phancongid)
        if not assignment:
            return jsonify({"message": "Không tìm thấy phân công công việc"}), 400
        # Lấy số lượng câu hỏi từ bảng congviec
        congviec_obj = congviec.query.get(assignment.congviecid)
        soluongcauhoi = congviec_obj.soluongcauhoi if congviec_obj else 0
        if so_cau >= soluongcauhoi:
            return jsonify({"message": "Không thể thêm quá số lượng câu hỏi được giao!"}), 400
    return question_service.add_question(data)

@question_bp.route('/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    data = request.json
    return question_service.update_question(question_id, data)

@question_bp.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    question_service.delete_question(question_id)
    return jsonify({'message': 'Question deleted successfully'}), 204

@question_bp.route('/questions')
def get_questions():
    phancongid = request.args.get('phancongid')
    if phancongid:
        questions = QuestionService.get_questions_by_assignment(phancongid)
        return jsonify(questions)

@question_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    data, status = question_service.get_question_by_id(question_id)
    return jsonify(data), status

@question_bp.route('/questions/by_exam/<int:dethiid>', methods=['GET'])
def get_questions_by_exam(dethiid):
    questions = QuestionService.get_questions_by_exam(dethiid)
    return jsonify(questions), 200