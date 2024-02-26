from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import json

from services.productoService import getById, getByName
from services.carritoService import guardarInformacionProducto, eliminarInformacionProducto, obtenerValor
main = Blueprint('carritoRoute', __name__)

@main.route('/agregar', methods=['POST'])
@login_required
def add():
    if current_user.rol == 'admin':
        return redirect(url_for('homrAdmin'))
    
    if request.method == 'POST':
        producto_id = request.form['producto_id']
        existing_product = getById(producto_id)
        if existing_product:
            cantidad = int(existing_product.cantidad)
            if cantidad < 1:
                return redirect(url_for('productoRoute.getAll'))
            else:
                guardarInformacionProducto(current_user.nombre, current_user, existing_product)
                return redirect(url_for('productoRoute.getAll'))

        
    return redirect(url_for('productoRoute.getAll'))


@main.route('/', methods=['GET'])
@login_required
def carritoView():
    if current_user.rol == 'admin':
        return redirect(url_for('homrAdmin'))
    
    existe_carrito = obtenerValor(current_user.nombre)
    if existe_carrito:
        pro = existe_carrito['productos']
        return render_template('carrito/carrito.html', lista_productos=pro)
    else:
         return redirect(url_for('productoRoute.getAll'))


@main.route('/eliminar', methods=['POST'])
@login_required
def delete():
    if current_user.rol == 'admin':
        return redirect(url_for('homrAdmin'))
    
    if request.method == 'POST':
        producto_name = request.form['producto_name']
        existing_product = getByName(producto_name)
        if existing_product:
            eliminarInformacionProducto(current_user.nombre, existing_product)

    return redirect(url_for('productoRoute.getAll'))