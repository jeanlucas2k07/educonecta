from flask import Blueprint, render_template

docs_bp = Blueprint('docs' , __name__, url_prefix="/docs")

@docs_bp.get('/')
def docs():
    return render_template('docs.html')