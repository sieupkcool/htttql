from app.models import Khoa, db

class DepartmentService:
    def create_department(self, name):
        department = Khoa(ten=name)
        db.session.add(department)
        db.session.commit()
        return {"khoaid": department.khoaid, "ten": department.ten}

    def update_department(self, department_id, name):
        department = Khoa.query.get(department_id)
        if not department:
            return None
        department.ten = name
        db.session.commit()
        return {"khoaid": department.khoaid, "ten": department.ten}

    def delete_department(self, department_id):
        department = Khoa.query.get(department_id)
        if not department:
            return False
        db.session.delete(department)
        db.session.commit()
        return True

    def get_all_departments(self):
        departments = Khoa.query.all()
        return [{"khoaid": d.khoaid, "ten": d.ten} for d in departments]