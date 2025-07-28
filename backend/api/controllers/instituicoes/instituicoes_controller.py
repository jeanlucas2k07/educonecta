from api.utils.validators.cnpj_validator import VerificaCNPJ
from api.utils.validators.id_validator import id_validator
from api.utils.validators.admin_password_validator import admin_password_validator
from api.services.intituicoes.instituicoes_service import InstituicaoServices
from flask import jsonify, request

class InstituicaoControllers:
    
    @staticmethod
    def create_institcuiao_controller():
        data = request.get_json()
        
        tipo = data.get("tipo")
        nome = data.get("nome")
        endereco = data.get("endereco")
        responsavel = data.get("responsavel")
        identificador = data.get("identificador")
        descricao = data.get("descricao")
        image = data.get("image")

        
        if not tipo:
            return jsonify({'error': "O tipo é obrigatório"}), 400
        
        if not nome:
            return jsonify({'error': "O nome é obrigatório"}), 400
            
        
        if tipo.lower() not in ("ong", "escola"):
            return jsonify({"error": "Só aceitamos ongs e escolas"}), 400
        
        if not endereco:
            return jsonify({"error": "O endereço é obrigatório"}), 400
        
        if not identificador:
            return jsonify({"error": "O número de indentificação (cnpj ou inep) é obrigatório"}), 400
        
        if not responsavel:
            return jsonify({"error": "O nome do responsável é obrigatório"}), 400
        
        if not descricao:
            return jsonify({"error": "O nome do Descricao é obrigatório"}), 400
        
        if not image:
            return jsonify({"error": "O nome do image é obrigatório"}), 400
        
        
        if tipo.lower() == 'ong':
            if not VerificaCNPJ(identificador):
                return jsonify({"error": "CNPJ inválido"}), 400
            
        params = (tipo, nome, endereco, responsavel, identificador, descricao, image)
        
        try:
            InstituicaoServices.create_instituicao_service(params)
            
        except Exception as e:
            return jsonify({"error": f"Erro ao tentar adicionar a institução: {e}"}), 500
        
        return jsonify({"message": f"A {tipo} foi adicionada com êxito!"}), 201
            
    @staticmethod
    def get_instituicao_controller():
        try:
            resp = InstituicaoServices.get_instituicao_service()
            
            if not resp:
                return jsonify({"message": "Ainda não temos nenhuma instituição cadastrada"}), 200
            
            return jsonify({"insituições": resp}), 200
        
        except Exception as e:
            return jsonify({"error": f"erro ao comunicar com o banco de dados: {e}"}), 500
    
    @staticmethod
    def delete_instituicao_controller(id):
        if not id_validator("instituicao", id):
            return jsonify({"error": "id inexistente"}), 400
        
        try:
            if InstituicaoServices.delete_instituicao_service(id):
                return jsonify({"message": "deleção feita com sucesso"}), 204
            
            else:
                return jsonify({"error": "id not found"}), 404
            
        except Exception as e:
            return jsonify({"Error": f"erro ao tentar deletar a instiruição: {e}"}), 500
    
    @staticmethod
    def get_instituicao_by_id_controller(id):
        if not id_validator("instituicao", id):
            return jsonify({"error": "id inexistente"}), 400
        
        try:
            resp = InstituicaoServices.get_instituicao_by_id_service(id)
            
            if resp == []:
                return jsonify({"message": "Não temos nenhuma instituição com este id"}), 200
            
            return jsonify({"insituição": resp}), 200
        except Exception as e:
            return jsonify({"error": f"erro ao comunicar com o banco de dados: {e}"}), 500
        
    @staticmethod
    def get_escola_controller():
        try:
            resp = InstituicaoServices.get_escola_service()
            
            if resp == []:
                return jsonify({"message": "Ainda não temos nenhuma escola cadastrada"}), 200
            
            return jsonify({"escolas": resp}), 200
        except Exception as e:
            return jsonify({"error": f"erro ao comunicar com o banco de dados: {e}"}), 500
        
    @staticmethod
    def get_ong_controller():
        try:
            resp = InstituicaoServices.get_ong_service()
            
            if resp == []:
                return jsonify({"message": "Ainda não temos nenhuma ong cadastrada"}), 200
            
            return jsonify({"ongs": resp}), 200
        except Exception as e:
            return jsonify({"error": f"erro ao comunicar com o banco de dados: {e}"}), 500
                    
    @staticmethod
    def delete_all_instituicao_controller():
        data = request.get_json()
        password = data.get("admin_password")
        
        if not password:
            return jsonify({"error": "admin password is required"}), 400
        
        if not admin_password_validator(password):
            return jsonify({"error": "admin password is wrong"}), 401
        
        try:
            InstituicaoServices.delete_all_instituicao_service()
            return jsonify({"message": "dados deletados com sucesso!"}), 204
        except Exception as e:
            return jsonify({'error': f"erro ao tentar deletar dados: {e}"}), 500