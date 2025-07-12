from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    reservas = db.relationship('Reserva', backref='alumno', lazy=True)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.String(50), nullable=False)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumno.id'), nullable=False)
