from app.models import dethi, cauhoi, nguoidung, monhoc, db
from sqlalchemy import func

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
    
    from app.models import cauhoi, monhoc
from sqlalchemy import func

class StatisticsService:
    @staticmethod
    def get_completion_statistics():
        from app.models import chitietcongviec, giangvien
        from sqlalchemy import func
        results = (
            db.session.query(
                chitietcongviec.giangvienid,
                func.count(chitietcongviec.phancongid).label('total'),
                func.sum(func.case([(chitietcongviec.trangthai == 'Đã hoàn thành', 1)], else_=0)).label('completed')
            )
            .group_by(chitietcongviec.giangvienid)
            .all()
        )
        stats = []
        for gv_id, total, completed in results:
            stats.append({
                "giangvienid": gv_id,
                "total": total,
                "completed": completed,
                "completion_rate": round(completed/total*100, 2) if total else 0
            })
        return stats