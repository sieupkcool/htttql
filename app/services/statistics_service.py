from app.models import dethi, cauhoi, nguoidung, monhoc, db
from sqlalchemy import func, extract

class StatisticsService:
    @staticmethod
    def get_exam_statistics():
        total_exams = dethi.query.count()
        total_questions = cauhoi.query.count()
        total_users = nguoidung.query.count()

        return {
            "total_exams": total_exams,
            "total_questions": total_questions,
            "total_users": total_users
        }

    @staticmethod
    def get_question_difficulty_distribution():
        difficulty_distribution = (
            cauhoi.query
            .with_entities(cauhoi.difficulty, func.count(cauhoi.id))
            .group_by(cauhoi.difficulty)
            .all()
        )

        return {difficulty: count for difficulty, count in difficulty_distribution}

    @staticmethod
    def get_exam_statistics_by_user(user_id):
        exams_taken = dethi.query.filter(dethi.user_id == user_id).count()
        return {
            "exams_taken": exams_taken
        }
    
    @staticmethod
    def get_completion_statistics(kyhoc=None, giangvien=None):
        from app.models import chitietcongviec, congviec, db
        query = chitietcongviec.query

        if kyhoc:
            years = [int(y) for y in kyhoc.split('-')]
            query = query.filter(extract('year', chitietcongviec.ngayphancong).in_(years))
        if giangvien:
            query = query.filter(chitietcongviec.giangvienid == giangvien)

        total = query.count()
        completed = query.filter(chitietcongviec.trangthai == "Đã hoàn thành").count()

        # Lấy tên giảng viên nếu có
        title = "Tỷ lệ hoàn thành công việc"
        if kyhoc:
            title += f" ({kyhoc})"
        if giangvien:
            from app.models import nguoidung
            gv = nguoidung.query.get(giangvien)
            if gv:
                title += f", Giảng viên: {gv.hovaten}"

        return {
            "total": total,
            "completed": completed,
            "title": title
        }
    
    @staticmethod
    def get_exam_count(kyhoc, monhoc_id):
        query = dethi.query
        title = "Số lượng đề thi"
        # Lọc theo năm tạo nếu có chọn kỳ học
        if kyhoc:
            years = [int(y) for y in kyhoc.split('-')]
            query = query.filter(extract('year', dethi.ngaytao).in_(years))
            title += f" theo năm tạo ({', '.join(str(y) for y in years)})"
        if monhoc_id:
            query = query.filter(dethi.monhocid == monhoc_id)
            title += f", môn học ({monhoc_id})"

        # Nếu chỉ chọn kỳ học, thống kê theo môn
        if kyhoc and not monhoc_id:
            result = (
                query.join(monhoc, dethi.monhocid == monhoc.monhocid)
                .with_entities(monhoc.ten, func.count(dethi.dethiid))
                .group_by(monhoc.ten)
                .all()
            )
            labels = [r[0] for r in result]
            values = [r[1] for r in result]
        # Nếu chọn môn học, trả về tên môn và tổng số đề thi
        elif monhoc_id:
            mon = monhoc.query.get(monhoc_id)
            mon_name = mon.ten if mon else "Môn học"
            count = query.count()
            labels = [mon_name]
            values = [count]
        # Nếu không chọn gì, thống kê theo tất cả môn
        else:
            result = (
                query.join(monhoc, dethi.monhocid == monhoc.monhocid)
                .with_entities(monhoc.ten, func.count(dethi.dethiid))
                .group_by(monhoc.ten)
                .all()
            )
            labels = [r[0] for r in result]
            values = [r[1] for r in result]

        return {
            "labels": labels,
            "values": values,
            "title": title
        }