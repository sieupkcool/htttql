from flask import jsonify, request
from app.models import nguoidung, db

class UserService:
    @staticmethod
    def update_user(user_id, data):
        user = nguoidung.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        
        user.hovaten = data.get('hovaten', user.hovaten)
        user.email = data.get('email', user.email)
        user.sodienthoai = data.get('sodienthoai', user.sodienthoai)
        user.gioitinh = data.get('gioitinh', user.gioitinh)
        
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200

    @staticmethod
    def get_user(user_id):
        user = nguoidung.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        
        return jsonify({
            "userid": user.userid,
            "hovaten": user.hovaten,
            "email": user.email,
            "sodienthoai": user.sodienthoai,
            "gioitinh": user.gioitinh
        }), 200

    @staticmethod
    def delete_user(user_id):
        user = nguoidung.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200

    @staticmethod
    def create_user(data):
        new_user = nguoidung(
            hovaten=data['hovaten'],
            email=data['email'],
            sodienthoai=data.get('sodienthoai'),
            gioitinh=data.get('gioitinh'),
            username=data['username'],
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully", "userid": new_user.userid}), 201