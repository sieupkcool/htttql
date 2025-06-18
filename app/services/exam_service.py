from flask import jsonify, request
from app.models import dethi, db

class ExamService:
    @staticmethod
    def create_exam(data):
        new_exam = dethi(
            title=data.get('title'),
            description=data.get('description'),
            subject_id=data.get('subject_id'),
            semester=data.get('semester'),
            year=data.get('year')
        )
        db.session.add(new_exam)
        db.session.commit()
        return jsonify({"message": "Exam created successfully", "exam_id": new_exam.id}), 201

    @staticmethod
    def update_exam(exam_id, data):
        exam = dethi.query.get(exam_id)
        if not exam:
            return jsonify({"message": "Exam not found"}), 404
        
        exam.title = data.get('title', exam.title)
        exam.description = data.get('description', exam.description)
        exam.subject_id = data.get('subject_id', exam.subject_id)
        exam.semester = data.get('semester', exam.semester)
        exam.year = data.get('year', exam.year)

        db.session.commit()
        return jsonify({"message": "Exam updated successfully"}), 200

    @staticmethod
    def delete_exam(exam_id):
        exam = dethi.query.get(exam_id)
        if not exam:
            return jsonify({"message": "Exam not found"}), 404
        
        db.session.delete(exam)
        db.session.commit()
        return jsonify({"message": "Exam deleted successfully"}), 200

    @staticmethod
    def get_exam(exam_id):
        exam = dethi.query.get(exam_id)
        if not exam:
            return jsonify({"message": "Exam not found"}), 404
        
        return jsonify({
            "id": exam.id,
            "title": exam.title,
            "description": exam.description,
            "subject_id": exam.subject_id,
            "semester": exam.semester,
            "year": exam.year
        }), 200

   
    @staticmethod
    def get_all_exams():
        exams = dethi.query.all()
        return [{
            "dethiid": exam.dethiid,  # Sử dụng đúng tên thuộc tính
            "madethi": exam.madethi,
            "ghichu": exam.ghichu,
            "monhocid": exam.monhocid,
            "ngaytao": exam.ngaytao.strftime('%Y-%m-%d') if exam.ngaytao else None,
            "cautrucdethiid": exam.cautrucdethiid
        } for exam in exams]