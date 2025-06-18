from flask import jsonify, request
from app.models import dethi, db

class ExamService:
    
    @staticmethod
    def create_exam(data):
        try:
            # Tạo đối tượng đề thi mới
            new_exam = dethi(
                madethi=data.get('madethi'),
                ghichu=data.get('ghichu'),
                monhocid=int(data.get('monhocid')) if data.get('monhocid') else None,
                ngaytao=data.get('ngaytao'),
                cautrucdethiid=int(data.get('cautrucdethiid')) if data.get('cautrucdethiid') else None,
                filedethi=None,  # Giá trị mặc định là NULL
                nguoitaoid=None  # Giá trị mặc định là NULL
            )
            # Thêm vào cơ sở dữ liệu
            db.session.add(new_exam)
            db.session.commit()
            return {
                "message": "Exam created successfully",
                "dethiid": new_exam.dethiid
            }
        except Exception as e:
            db.session.rollback()
            return {
                "message": "Error creating exam",
                "error": str(e)
            }

    @staticmethod
    def update_exam(exam_id, data):
        exam = dethi.query.get(exam_id)
        if not exam:
            return jsonify({"message": "Exam not found"}), 404
        
        exam.madethi = data.get('madethi', exam.madethi)
        exam.ghichu = data.get('ghichu', exam.ghichu)
        exam.monhocid = data.get('monhocid', exam.monhocid)
        exam.ngaytao = data.get('ngaytao', exam.ngaytao)
        exam.cautrucdethiid = data.get('cautrucdethiid', exam.cautrucdethiid)

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
            "dethiid": exam.dethiid,
            "madethi": exam.madethi,
            "ghichu": exam.ghichu,
            "monhocid": exam.monhocid,
            "ngaytao": exam.ngaytao.strftime('%Y-%m-%d') if exam.ngaytao else None,
            "cautrucdethiid": exam.cautrucdethiid
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