from database.connection import execute_query

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
    