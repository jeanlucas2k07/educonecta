from database.connection import execute_query

class InstituicaoServices:
    @staticmethod
    def __response(query):
        rows = execute_query(query)
        if rows:
            row = [
                {"id": r[0], "tipo": r[1], "endereco": r[2], "responsavel": r[3], "cod_identificador": r[4]} for r in rows
            ]
            return row
        else:
            return []
        
    @staticmethod
    def create_instituicao_service(params):
        query = """
            INSERT INTO instituicao (tipo, endereco, nome_respnsavel, identificador) VALUES (%s, %s, %s, %s)
        """   
        execute_query(query, params)
        
    @staticmethod
    def get_instituicao_service(params=None):
        if params == None:
            return InstituicaoServices.__response("SELECT * FROM instituicao")
    
    @staticmethod
    def get_escola_service(params = None):
        if params == None:
            return InstituicaoServices.__response("SELECT * FROM instituicao WHERE tipo = 'escola'")
        
    @staticmethod
    def get_ong_service(params = None):
        if params == None:
            return InstituicaoServices.__response("SELECT * FROM instituicao WHERE tipo = 'escola'")