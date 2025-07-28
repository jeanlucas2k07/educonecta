from api.database.connection import execute_query 

def id_validator(table: str, id: int):
    try:
        query = f"SELECT id_inst FROM {table} WHERE id_inst = %s"
        result = execute_query(query, (id,))
        
        return bool(result)
    except Exception as e:
        print("erro ao validar:", e)
        return False