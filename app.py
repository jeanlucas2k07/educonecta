from flask import Flask
from database.init_databases import init_databases
from routes.home import home
from services.instituicoes_services import (
    all_ongs, 
    all_escolas, 
    all_intituicoes,
    add_instituicao
)
init_databases()

app = Flask(__name__)

## ROTAS GET ##

@app.get("/")
def home_route():
    return home()

@app.get("/instituicoes")
def return_instituicoes():
    return all_intituicoes()

@app.get("/escolas")
def return_escolas():
    return all_escolas()

@app.get("/ong")
def return_ongs():
    return all_ongs()

## ROTAS POST ##

@app.post("/add_instituicao")
def add_instituicao():
    return add_instituicao()

## ROTAS PUT ##

## ROTAS DELETE ##


