import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def open_connection():
    return psycopg2.connect(DATABASE_URL)

def execute_query(query, params=None):
    conn = open_connection()
    conn.set_client_encoding('UTF8')
    
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                result = cur.fetchall()
            else:
                conn.commit()
                result = None
            
        return result
    finally:
        conn.close()
