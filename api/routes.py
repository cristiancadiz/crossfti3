from flask import Blueprint, render_template, request, redirect, url_for, flash
import os

main = Blueprint('main', __name__)
ARCHIVO_RESERVAS = "reservas.txt"

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

        with open(ARCHIVO_RESERVAS, "a", encoding="utf-8") as f:
            f.write(f"{nombre} | {email} | {horario}\n")

        flash("✅ Reserva guardada exitosamente.")
        return redirect(url_for('main.home'))

    return render_template("reserva.html", horarios=horarios)

@main.route('/reservas')
def ver_reservas():
    if not os.path.exists(ARCHIVO_RESERVAS):
        reservas = []
    else:
        with open(ARCHIVO_RESERVAS, "r", encoding="utf-8") as f:
            reservas = [line.strip() for line in f.readlines()]
    return render_template("ver_reservas.html", reservas=reservas)
