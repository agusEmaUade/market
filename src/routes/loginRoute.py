from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

from models.usuario import Usuario
from services.usuarioService import authenticate, create, getByUsername, getById, update, getAllBuyers, delete

main = Blueprint('loginRoute', __name__)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuario = authenticate(username, password)
        if usuario:
            login_user(usuario)
            flash('Inicio de sesión exitoso!', 'success')

            if usuario.rol != 'admin':
                return redirect(url_for('productoRoute.getAll'))
            else:
                return redirect(url_for('homrAdmin'))
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


@main.route('/datos_personales', methods=['GET', 'POST'])
@login_required
def updateUser():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        existing_user = getByUsername(username)
        if existing_user:
            flash('El nombre de usuario ya está en uso.', 'error')
            return redirect(url_for('loginRoute.updateUser'))
        else:
            update(current_user.id, password, email, username)
            flash('¡Cuenta actualizada con éxito!', 'success')
            return redirect(url_for('loginRoute.updateUser'))
    else:
        usuarioBd = getById(current_user.id)
        return render_template('login/modificarUsuario.html', usuario=usuarioBd)
    

@main.route('/abm/delete', methods=['POST'])
@login_required
def deleteUser():
    if current_user.rol != 'admin':
        return redirect(url_for('logout'))

    usuario_id = request.form['usuario_id']
    existing_user = getById(usuario_id)
    if existing_user:
        delete(usuario_id)
        return redirect(url_for('loginRoute.viewUser'))
    else:
        return redirect(url_for('loginRoute.viewUser'))
    

@main.route('/abm', methods=['GET'])
@login_required
def viewUser():
    if current_user.rol != 'admin':
        return redirect(url_for('logout'))
    
    usuarios = getAllBuyers()
    return render_template('login/abmUsuarios.html', lista_usuarios=usuarios)