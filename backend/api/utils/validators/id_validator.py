from api.database.connection import execute_query 

def id_validator(table: str, id: int):
    try:
        query = f"SELECT id FROM {table} WHERE id = %s"
        result = execute_query(query, (id,))
        
        return bool(result)
    except Exception as e:
        print("erro ao validar:", e)
        return False