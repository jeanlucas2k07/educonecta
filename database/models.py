import os
import psycopg2

class Database_Connection:
    DATABASE_URL = os.getenv("DATABASE_URL")
    API_KEY = os.getenv("API_KEY")
    conn = psycopg2.connect(DATABASE_URL)