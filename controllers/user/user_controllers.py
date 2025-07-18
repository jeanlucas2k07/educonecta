from utils.validators.email_validator import email_validator
from utils.validators.password_validator import password_validator
from services.user.user_services import UserServices
from flask import request, jsonify

class UserControlls:
    @staticmethod
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
        
        if UserServices.create_user_service(user_data):
            return jsonify({"message": "usuário criado com sucesso!"}), 201
        
        else:
            return jsonify({"Error": "erro ao criar usuário"}), 500
        
    @staticmethod
    def get_user_controller():
        try:
            query = "SELECT * FROM users"
            resp = UserServices.get_user_services(query)
            
            if resp == []:
                return jsonify({"message": "ainda sem usuários cadastrados"}), 200
            else:
                return jsonify(resp), 200
            
        except Exception as e:
            return jsonify({"error": f"erro ao consultar a tebela: {e}"}), 500