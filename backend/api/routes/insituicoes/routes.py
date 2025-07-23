from api.controllers.instituicoes.instituicoes_controller import InstituicaoControllers
from flask import Blueprint

instituicoes_bp = Blueprint("instituicoes", __name__, url_prefix="/instituicoes")

@instituicoes_bp.get("/")
def get_instituicoes():
    return InstituicaoControllers.get_instituicao_controller()

@instituicoes_bp.get("/<int:id>")
def get_instituicoes_by_id(id):
    return InstituicaoControllers.get_instituicao_by_id_controller(id)

@instituicoes_bp.get("/escolas")
def get_scolas():
    return InstituicaoControllers.get_escola_controller()

@instituicoes_bp.get("/ongs")
def get_ongs():
    return InstituicaoControllers.get_ong_controller()

@instituicoes_bp.post("/")
def create_instituicao():
    return InstituicaoControllers.create_institcuiao_controller()

@instituicoes_bp.delete("/<int:id>")
def delete_instituicao(id):
    return InstituicaoControllers.delete_instituicao_controller(id)

@instituicoes_bp.delete("/")
def delete_all_instituicoes():
    return InstituicaoControllers.delete_all_instituicao_controller()