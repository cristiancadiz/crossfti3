from flask import Flask
from api.routes import main
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave-secreta")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///clases.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from api import models  # Importar modelos después de instanciar db
models.db = db

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(main)

@app.before_first_request
def crear_tablas():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
