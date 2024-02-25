from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

from models.usuario import Usuario
from services.usuarioService import authenticate, create, getByUsername

main = Blueprint('loginRoute', __name__)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuario = Usuario.get_by_username(username)
        if usuario and check_password_hash(usuario.password_hash, password):
            login_user(usuario)
            flash('Inicio de sesión exitoso!', 'success')
            return redirect(url_for('productoRoute.getAll'))
        else:
            flash('Nombre de usuario o contraseña incorrectos.', 'error')
    return render_template('login/login.html')


@main.route('/crear', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        existing_user = getByUsername(username)
        if existing_user:
            flash('El nombre de usuario ya está en uso.', 'error')
            return redirect(url_for('index'))
        else:
            create(username, password, email)
            flash('¡Cuenta creada con éxito! Por favor inicia sesión.', 'success')
            return redirect(url_for('index'))
    return render_template('login/crearUsuario.html')
