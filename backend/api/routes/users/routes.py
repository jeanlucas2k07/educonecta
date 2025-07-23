from api.controllers.users.users_controller import UserControllers

from flask import Blueprint

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.get("/")
def get_users_bp():
    return UserControllers.get_user_controller()

@users_bp.get("/<int:id>")
def get_users_by_id_bp(id):
    return UserControllers.get_user_by_id_controller(id)

@users_bp.post("/")
def create_user_bp():
    return UserControllers.create_user_controller()

@users_bp.put("/<int:id>")
def update_user_bp(id):
    return UserControllers.update_user_controller(id)

@users_bp.delete("/<int:id>")
def delete_user_bp(id):
    return UserControllers.delete_user_controller(id)