from flask import Blueprint, render_template, request, redirect, url_for, flash
from api.models import db, Alumno, Reserva

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/reservar', methods=['GET', 'POST'])
def reservar():
    horarios = ["Lunes 10:00", "Martes 14:00", "Miércoles 16:00"]
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        horario = request.form['horario']

        alumno = Alumno.query.filter_by(email=email).first()
        if not alumno:
            alumno = Alumno(nombre=nombre, email=email)
            db.session.add(alumno)
            db.session.commit()

        nueva_reserva = Reserva(horario=horario, alumno_id=alumno.id)
        db.session.add(nueva_reserva)
        db.session.commit()

        flash("Reserva guardada exitosamente.")
        return redirect(url_for('main.home'))

    return render_template("reserva.html", horarios=horarios)
