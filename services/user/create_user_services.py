from database.connection import execute_query


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