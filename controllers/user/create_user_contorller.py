from utils.validators.email_validator import email_validator
from utils.validators.password_validator import password_validator
from services.user.create_user_services import create_user_service
from flask import request, jsonify

def create_user_controller():
    data = request.get_json()
    
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    
    if not name:
        return jsonify({"Error": "O nome é obrigatório"}), 400

    if not email or not email_validator(email):
        return jsonify({"Error": "email inválido"}), 400
    
    if not password or not password_validator(password):
        return jsonify({"Error": "senha inválida"}), 400
    
    user_data = (name, email, password)
    
    if create_user_service(user_data):
        return jsonify({"message": "usuário criado com sucesso!"}), 201
    
    else:
        return jsonify({"Error": "erro ao criar usuário"}), 500