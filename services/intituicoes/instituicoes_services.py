from database.connection import execute_query

class InstituicaoServices:
    @staticmethod
    def __response(query, params=None):
        rows = execute_query(query, params)
        if rows:
            row = [
                {"id": r[0], "tipo": r[1], "nome": r[2], "endereco": r[3], "responsavel": r[4], "cod_identificador": r[5]} for r in rows
            ]
            return row
        else:
            return []
        
    @staticmethod
    def create_instituicao_service(params):
        query = """
            INSERT INTO instituicao (tipo, nome, endereco, responsavel, identificador) VALUES (%s, %s, %s, %s, %s)
        """   
        execute_query(query, params)
        
    @staticmethod
    def get_instituicao_service(params=None):
        if params == None:
            return InstituicaoServices.__response("SELECT * FROM instituicao")
        
    @staticmethod
    def get_instituicao_by_id_service(id):
        return InstituicaoServices.__response("SELECT * FROM instituicao WHERE id_inst = %s", id)
    
    @staticmethod
    def get_escola_service(params = None):
        if params == None:
            return InstituicaoServices.__response("SELECT * FROM instituicao WHERE tipo = 'escola'")
        
    @staticmethod
    def get_ong_service(params = None):
        if params == None:
            return InstituicaoServices.__response("SELECT * FROM instituicao WHERE tipo = 'ong'")
        
    @staticmethod
    def delete_instituicao_service(id):
        try:
            id = int(id)
            
        except ValueError:
            return False
        
        rows = execute_query("SELECT id_inst FROM instituicao")
        
        if rows:
            ids = [r[0] for r in rows]
            if id not in ids:
                return False
        
        execute_query("DELETE FROM instituicao WHERE id_inst = %s", (id,))
        return True