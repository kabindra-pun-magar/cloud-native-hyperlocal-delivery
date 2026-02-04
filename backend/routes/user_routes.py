from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/user", methods=["POST"])
def create_user():
    data = request.json
    user = User(name=data["name"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"})

@user_bp.route("/user", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])
