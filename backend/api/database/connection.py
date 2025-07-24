import os
import psycopg2
from dotenv import load_dotenv
from api.database import ip_validator

load_dotenv()


try:
    if ip_validator() == "IPv4":
        DATABASE_URL = os.getenv("DATABASE_URL_IPV4")
        
    elif ip_validator() == "IPv6":
        DATABASE_URL = os.getenv("DATABASE_URL_IPV6")    
except Exception:
    print("error: ", Exception)


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
    
    except Exception as e:
        return print(f"error: {e}")
    
    finally:
        conn.close()
