from flask_cors import CORS
from flask import render_template
from api import create_app

app = create_app()
CORS(app)

@app.get("/")
def home_route():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()