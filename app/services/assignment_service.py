from app.models import chitietcongviec,cauhoi, congviec, db

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

    @staticmethod
    def get_assignments_for_giangvien(giangvienid):
        assignments = chitietcongviec.query.filter_by(giangvienid=giangvienid).all()
        result = []
        for a in assignments:
            # Lấy số lượng câu hỏi từ bảng congviec
            congviec_obj = congviec.query.get(a.congviecid)
            soluongcauhoi = congviec_obj.soluongcauhoi if congviec_obj else 0
            # Đếm số câu hỏi đã thêm cho công việc này
            so_cau = cauhoi.query.filter_by(phancongid=a.phancongid).count()
            result.append({
                "phancongid": a.phancongid,
                "congviecid": a.congviecid,
                "soluongcauhoi": soluongcauhoi,
                "soluongdatham": so_cau,
                "trangthai": a.trangthai
            })
        return result