from flask import Blueprint


user_bp = Blueprint("user", __name__, url_prefix="/users")

@user_bp.route("/profile")
def profile():
    return ""