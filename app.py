from flask import Flask, request
from database.init_databases import init_databases
from routes.home import home
from controllers.instituicoes.instituicao_controller import InstituicaoControllers
from controllers.user.create_user_contorller import create_user_controller
from controllers.user.get_user_controller import get_user_controller

init_databases()

app = Flask(__name__)

## ROTAS GET ##

@app.get("/")
def home_route():
    return home()

@app.get("/instituicoes")
def get_instituicoes_route():
    return InstituicaoControllers.get_instituicao_controller()

@app.get("/escolas")
def return_escolas():
    return InstituicaoControllers.get_escola_controller()

@app.get("/ong")
def return_ongs():
    return InstituicaoControllers.get_ong_controller()

@app.get("/users")
def get_user_route():
    return get_user_controller()

## ROTAS POST ##

@app.post("/instituicao")
def create_instituicao_route():
    return InstituicaoControllers.create_institcuiao_controller()

@app.post("/users")
def create_user_route():
    return create_user_controller()
    

## ROTAS PUT ##


## ROTAS DELETE ##


