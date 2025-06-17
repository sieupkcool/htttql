from app.models import monhoc, db

class SubjectService:
    def create_subject(self, data):
        subject = monhoc(
            ten=data.get('ten'),
            mamon=data.get('mamon'),
            sochuong=data.get('sochuong'),
            socauhoide=data.get('socauhoide'),
            socauhoikho=data.get('socauhoikho'),
            socauhoi=data.get('socauhoi'),
            bomonid=data.get('bomonid')
        )
        db.session.add(subject)
        db.session.commit()
        return {
            "monhocid": subject.monhocid,
            "ten": subject.ten,
            "mamon": subject.mamon,
            "sochuong": subject.sochuong,
            "socauhoide": subject.socauhoide,
            "socauhoikho": subject.socauhoikho,
            "socauhoi": subject.socauhoi,
            "bomonid": subject.bomonid
        }

    def update_subject(self, subject_id, data):
        subject = monhoc.query.get(subject_id)
        if not subject:
            return None
        subject.ten = data.get('ten', subject.ten)
        subject.mamon = data.get('mamon', subject.mamon)
        subject.sochuong = data.get('sochuong', subject.sochuong)
        subject.socauhoide = data.get('socauhoide', subject.socauhoide)
        subject.socauhoikho = data.get('socauhoikho', subject.socauhoikho)
        subject.socauhoi = data.get('socauhoi', subject.socauhoi)
        subject.bomonid = data.get('bomonid', subject.bomonid)
        db.session.commit()
        return {
            "monhocid": subject.monhocid,
            "ten": subject.ten,
            "mamon": subject.mamon,
            "sochuong": subject.sochuong,
            "socauhoide": subject.socauhoide,
            "socauhoikho": subject.socauhoikho,
            "socauhoi": subject.socauhoi,
            "bomonid": subject.bomonid
        }

    def delete_subject(self, subject_id):
        subject = monhoc.query.get(subject_id)
        if not subject:
            return False
        db.session.delete(subject)
        db.session.commit()
        return True

    def get_all_subjects(self):
        subjects = monhoc.query.all()
        return [{
            "monhocid": s.monhocid,
            "ten": s.ten,
            "mamon": s.mamon,
            "sochuong": s.sochuong,
            "socauhoide": s.socauhoide,
            "socauhoikho": s.socauhoikho,
            "socauhoi": s.socauhoi,
            "bomonid": s.bomonid
        } for s in subjects]

    def get_subject_by_id(self, subject_id):
        s = monhoc.query.get(subject_id)
        if not s:
            return None
        return {
            "monhocid": s.monhocid,
            "ten": s.ten,
            "mamon": s.mamon,
            "sochuong": s.sochuong,
            "socauhoide": s.socauhoide,
            "socauhoikho": s.socauhoikho,
            "socauhoi": s.socauhoi,
            "bomonid": s.bomonid
        }