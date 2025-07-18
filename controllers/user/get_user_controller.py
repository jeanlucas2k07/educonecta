from flask import jsonify
from services.user.get_user_services import get_user_services

def get_user_controller():
    try:
        query = "SELECT * FROM users"
        resp = get_user_services(query)
        
        if resp == []:
            return jsonify({"message": "ainda sem usuários cadastrados"}), 200
        else:
            return jsonify(resp), 200
        
    except Exception as e:
        return jsonify({"error": f"erro ao consultar a tebela: {e}"}), 500