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
        if giangvienid:
            assignments = chitietcongviec.query.filter_by(giangvienid=giangvienid).all()
        else:
            assignments = chitietcongviec.query.all()
        result = []
        for a in assignments:
            congviec_obj = congviec.query.get(a.congviecid)
            soluongcauhoi = congviec_obj.soluongcauhoi if congviec_obj else 0
            noidung = congviec_obj.noidung if congviec_obj else None
            so_cau = cauhoi.query.filter_by(phancongid=a.phancongid).count()
            result.append({
                "phancongid": a.phancongid,
                "giangvienid": a.giangvienid,
                "congviecid": a.congviecid,
                "noidung": noidung,
                "soluongcauhoi": soluongcauhoi,
                "soluongdatham": so_cau,
                "trangthai": a.trangthai
            })
        return result

    def create_task(self, data):
        task = congviec(
            noidung=data.get('noidung'),
            soluongcauhoi=int(data.get('soluongcauhoi')) if data.get('soluongcauhoi') else None,
            truongbomonid=int(data.get('truongbomonid')) if data.get('truongbomonid') else None,
            monhocid=int(data.get('monhocid')) if data.get('monhocid') else None
        )
        db.session.add(task)
        db.session.commit()
        return {
            "congviecid": task.congviecid,
            "noidung": task.noidung,
            "soluongcauhoi": task.soluongcauhoi,
            "truongbomonid": task.truongbomonid,
            "monhocid": task.monhocid
        }