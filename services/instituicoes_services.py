from database.connection import execute_query
from flask import jsonify

def response(query):
    row = execute_query(query)
    
    if row:
        return jsonify({"inst": row})
    else:
        return jsonify({"inst": "ainda tá sem"})

def all_intituicoes():
    return response("SELECT * FROM instituicao")
    
def all_escolas():
    return response("SELECT * FROM escola")

def all_ongs():
    return response("SELECT * FROM ongs")


def add_instituicao():
    ...