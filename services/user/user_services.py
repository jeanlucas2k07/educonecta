from database.connection import execute_query


class UserServices:
    @staticmethod
    def create_user_service(data):
        params = tuple(data)
        try:
            query = """
            INSERT INTO users (name, email, password) VALUES (%s, %s, %s)
            """
            execute_query(query, params)
            return True
        
        except:
            return False
    
    @staticmethod
    def get_user_services(query, params = None):
        rows = execute_query(query, params)
        
        if rows:
            row = [
                {
                    "id": r[0],
                    "name": r[1],
                    "email": r[2],
                    "password": r[3],
                    "created_at": r[4]
                } for r in rows
            ]
            
            return row
        
        else:
            return []
    