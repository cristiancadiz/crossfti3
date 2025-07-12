from flask import Flask
from api.routes import main
from flask_sqlalchemy import SQLAlchemy
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

app.register_blueprint(main)

# Crear tablas automáticamente
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
