from flask import jsonify, request
from app.models import cauhoi, db

class QuestionService:
    @staticmethod
    def add_question(data):
        new_question = cauhoi(
            mota=data.get('mota'),
            mucdo=data.get('mucdo'),
            chuong=data.get('chuong'),
            nguoitaoid=data.get('nguoitaoid'),
            dethiid=data.get('dethiid')
        )
        db.session.add(new_question)
        db.session.commit()
        return jsonify({"message": "Question added successfully", "cauhoiid": new_question.cauhoiid}), 201

    @staticmethod
    def update_question(question_id, data):
        question = cauhoi.query.get(question_id)
        if not question:
            return jsonify({"message": "Question not found"}), 404
        
        question.mota = data.get('mota', question.mota)
        question.mucdo = data.get('mucdo', question.mucdo)
        question.chuong = data.get('chuong', question.chuong)
        question.nguoitaoid = data.get('nguoitaoid', question.nguoitaoid)
        question.dethiid = data.get('dethiid', question.dethiid)
        
        db.session.commit()
        return jsonify({"message": "Question updated successfully"}), 200

    @staticmethod
    def delete_question(question_id):
        question = cauhoi.query.get(question_id)
        if not question:
            return jsonify({"message": "Question not found"}), 404
        
        db.session.delete(question)
        db.session.commit()
        return jsonify({"message": "Question deleted successfully"}), 200

    @staticmethod
    def get_all_questions():
        questions = cauhoi.query.all()
        return jsonify([{
            "cauhoiid": q.cauhoiid,
            "mota": q.mota,
            "mucdo": q.mucdo,
            "chuong": q.chuong,
            "nguoitaoid": q.nguoitaoid,
            "dethiid": q.dethiid
        } for q in questions]), 200

    @staticmethod
    def get_question_by_id(question_id):
        question =  cauhoi.query.get(question_id)
        if not question:
            return jsonify({"message": "Question not found"}), 404
        return jsonify({
            "cauhoiid": question.cauhoiid,
            "mota": question.mota,
            "mucdo": question.mucdo,
            "chuong": question.chuong,
            "nguoitaoid": question.nguoitaoid,
            "dethiid": question.dethiid
        }), 200