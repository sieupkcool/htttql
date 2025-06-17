from app.models import chitietcongviec, db

class AssignmentService:
    def create_assignment(self, data):
        assignment = chitietcongviec(
            giangvienid=data.get('giangvienid'),
            congviecid=data.get('congviecid'),
            ghichu=data.get('ghichu'),
            ngayphancong=data.get('ngayphancong'),
            trangthai=data.get('trangthai')
        )
        db.session.add(assignment)
        db.session.commit()
        return {
            "phancongid": assignment.phancongid,
            "giangvienid": assignment.giangvienid,
            "congviecid": assignment.congviecid,
            "ghichu": assignment.ghichu,
            "ngayphancong": str(assignment.ngayphancong),
            "trangthai": assignment.trangthai
        }

    def get_assignment(self, assignment_id):
        assignment = chitietcongviec.query.get(assignment_id)
        if not assignment:
            return None
        return {
            "phancongid": assignment.phancongid,
            "giangvienid": assignment.giangvienid,
            "congviecid": assignment.congviecid,
            "ghichu": assignment.ghichu,
            "ngayphancong": str(assignment.ngayphancong),
            "trangthai": assignment.trangthai
        }

    def update_assignment(self, assignment_id, data):
        assignment = chitietcongviec.query.get(assignment_id)
        if not assignment:
            return None
        assignment.ghichu = data.get('ghichu', assignment.ghichu)
        assignment.ngayphancong = data.get('ngayphancong', assignment.ngayphancong)
        assignment.trangthai = data.get('trangthai', assignment.trangthai)
        db.session.commit()
        return {
            "phancongid": assignment.phancongid,
            "giangvienid": assignment.giangvienid,
            "congviecid": assignment.congviecid,
            "ghichu": assignment.ghichu,
            "ngayphancong": str(assignment.ngayphancong),
            "trangthai": assignment.trangthai
        }

    def delete_assignment(self, assignment_id):
        assignment = chitietcongviec.query.get(assignment_id)
        if not assignment:
            return False
        db.session.delete(assignment)
        db.session.commit()
        return True