from flask import Flask, jsonify
from flask_cors import CORS
from database.init_databases import init_databases
from routes.home import home
from controllers.instituicoes.instituicao_controller import InstituicaoControllers
from controllers.user.user_controllers import UserControllers

init_databases()

app = Flask(__name__)
CORS(app)


## ROTAS GET ##

@app.get("/")
def home_route():
    return home()

@app.get("/instituicao")
def get_instituicoes_route():
    return InstituicaoControllers.get_instituicao_controller()

@app.get("/instituicao/<id>")
def get_instituicao_by_id_route(id):
    return InstituicaoControllers.get_instituicao_by_id_controller(id)

@app.get("/escolas")
def get_escolas_route():
    return InstituicaoControllers.get_escola_controller()

@app.get("/ong")
def return_ongs():
    return InstituicaoControllers.get_ong_controller()

@app.get("/users")
def get_user_route():
    return UserControllers.get_user_controller()

@app.get("/users/<id>")
def get_user_by_id_route(id):
    return UserControllers.get_user_by_id_controller(id)



## ROTAS POST ##

@app.post("/instituicao")
def create_instituicao_route():
    return InstituicaoControllers.create_institcuiao_controller()

@app.post("/users")
def create_user_route():
    return UserControllers.create_user_controller()
    

## ROTAS PUT ##
@app.put("/users/<id>")
def update_user_route(id):
    return UserControllers.update_user_controller(id)

## ROTAS DELETE ##
@app.delete("/instituicao/<id>")
def delete_instituicao_route(id):
    return InstituicaoControllers.delete_instituicao_controller(id)

@app.delete("/users/<id>")
def delete_user_route(id):
    return UserControllers.delete_user_controller(id)

if __name__ == "__main__":
    app.run()