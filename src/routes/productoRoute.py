from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_required, logout_user, current_user
from services.productoService import getAllActive, getById, getByName, delete, update, create


main = Blueprint('productoRoute', __name__)

@main.route('/', methods=['GET'])
@login_required
def getAll():
    return render_template('producto/catalogo.html', productos=getAllActive())


@main.route('/abm', methods=['GET'])
@login_required
def getView():
    if current_user.rol != 'admin':
        return redirect(url_for('logout'))
    
    return render_template('producto/producto.html', lista_productos=getAllActive())


@main.route('/abm/agregar', methods=['POST'])
@login_required
def agregarProducto():
    if current_user.rol != 'admin':
        return redirect(url_for('logout'))
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']

        existing_product = getByName(nombre)
        if existing_product:
          flash('El nombre de producto ya está en uso.', 'error')
          return redirect(url_for('productoRoute.getView'))
        else:
          create(nombre, descripcion, precio)
          flash('¡Producto creada con éxito!.', 'success')
          return redirect(url_for('productoRoute.getView'))
    
    return redirect(url_for('productoRoute.getView'))


@main.route('/abm/eliminar/<producto_id>', methods=['POST'])
def eliminarProducto(producto_id):
    if request.method == 'POST':
      existing_product = getById(producto_id)
      if existing_product:
          delete(producto_id)
          flash('Producto eliminado correctamente', 'success')
          return redirect(url_for('productoRoute.getView'))
      else:
        flash('Error al eliminar producto. Producto no encontrado.', 'error')
        return redirect(url_for('productoRoute.getView'))  
      
    return  redirect(url_for('productoRoute.getView'))


@main.route('/abm/actualizar/<producto_id>', methods=['POST'])
def actualizarProducto(producto_id):
    if request.method == 'POST':
        nuevo_nombre = request.form['nombre-producto-nuevo']
        existing_product = getById(producto_id)
        if existing_product:
            existing_product.nombre = nuevo_nombre
            update(nuevo_nombre,None, None)
            flash('Producto actualizado correctamente', 'success')
            return redirect(url_for('productoRoute.getView'))
        else:
            flash('Error al actualizar producto. Producto no encontrado.', 'error')
            return redirect(url_for('productoRoute.getView'))
    return  redirect(url_for('productoRoute.getView'))