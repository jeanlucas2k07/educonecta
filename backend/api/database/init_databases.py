from api.database.connection import execute_query
import glob
import os

def get_schemas():
    dir = "./scripts_db"
    scripts = list()
    schemas = glob.glob(os.path.join(dir, '*.sql'))

    for schema in schemas:
        with open(schema, "r", encoding="utf-8") as f:
            scripts.append(f.read())
    
    return tuple(scripts)

def init_databases():
    for schema in get_schemas():
        execute_query(schema)

            
