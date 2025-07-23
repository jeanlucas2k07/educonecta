from api.routes.users.routes import users_bp
from api.routes.insituicoes.routes import instituicoes_bp
from api.routes.docs.routes import docs_bp
from api.database.init_databases import init_databases
from flask import Flask

def create_app():
    app = Flask(__name__, static_folder="static")
    init_databases()
    
    app.register_blueprint(users_bp)
    app.register_blueprint(instituicoes_bp)
    app.register_blueprint(docs_bp)
    return app