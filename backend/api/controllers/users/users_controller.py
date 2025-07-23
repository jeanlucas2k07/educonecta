from api.utils.validators.email_validator import email_validator
from api.utils.validators.password_validator import password_validator
from api.utils.validators.id_validator import id_validator
from api.services.users.users_service import UserServices
from flask import request, jsonify

class UserControllers:
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
        
        try:
            user_data = (name, email, password)
            UserServices.create_user_service(user_data)
            return jsonify({"message": "usuário criado com sucesso!"}), 201
        
        except Exception as e:
            return jsonify({"Error": "erro ao criar usuário: {e}"}), 500
        
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
        
    @staticmethod
    def get_user_by_id_controller(id):
        if not id_validator("users", id):
            return ({"error": "id inexistente"}), 400
        try:
            query = "SELECT * FROM users WHERE id = %s"
            resp = UserServices.get_user_services(query, (id,))
            
            return jsonify(resp), 200
        except Exception as e:
            return jsonify({"error": f"erro ao buscar o usuário: {e}"}), 500
        
    @staticmethod
    def update_user_controller(id_value):
            
        data = request.get_json()
        
        column = data.get("column")
        update = data.get("update")
        
        if not id_validator("users", id_value):
            return jsonify({"error": "id inexistente"}), 400
        
        if column not in ("email", "password", "name"):
            return jsonify ({"error": "insira uma coluna válida"}), 400
        
        if column == "password":
            if not password_validator(update):
                return jsonify({"error": "senha inválida"}), 400
        
        if column == "email":
            if not email_validator(update):
                return jsonify({"error": "email inválida"}), 400
            
        try:
            UserServices.update_user_services(column, update, id)
            return jsonify({"message": "usuário alterado com sucesso"}), 200
        except Exception as e:
            return jsonify({"error": f"erro no banco de dados: {e}"}), 500
    
    @staticmethod
    def delete_user_controller(id):
        if not id_validator("users", id):
            return jsonify({"error": "id inexistente"}), 400
        
        try:
            UserControllers.delete_user_controller(id)
            return jsonify({"message": "usuário deletado com sucesso"}), 204
        except Exception as e:
            return jsonify({"error": f"erro no banco de dados: {e}"}), 500
            
        
