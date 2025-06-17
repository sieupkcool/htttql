from flask import jsonify, request
from app.models import cauhoi, db

class QuestionService:
    @staticmethod
    def add_question(data):
        import json
        if data.get('loaicauhoi') == 'tracnghiem':
            try:
                dapan_obj = json.loads(data.get('dapan'))
                assert 'option' in dapan_obj and 'choices' in dapan_obj
                assert len(dapan_obj['choices']) == 4
            except Exception:
                return jsonify({"message": "Đáp án trắc nghiệm không hợp lệ"}), 400
        elif data.get('loaicauhoi') == 'tuluan':
            try:
                dapan_obj = json.loads(data.get('dapan'))
                assert 'content' in dapan_obj
            except Exception:
                return jsonify({"message": "Đáp án tự luận không hợp lệ"}), 400

        # Đảm bảo luôn có trường noidung
        noidung = data.get('noidung') or data.get('mota')

        new_question = cauhoi(
            mota=data.get('mota'),
            mucdo=data.get('mucdo'),
            chuong=data.get('chuong'),
            loaicauhoi=data.get('loaicauhoi'),
            dapan=data.get('dapan'),
            nguoitaoid=data.get('nguoitaoid'),
            ngaytao=data.get('ngaytao'),
            noidung=noidung,  # Thêm dòng này
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