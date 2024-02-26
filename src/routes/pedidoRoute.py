from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import json

from services.productoService import getById, getByName, update
from services.carritoService import obtenerValor, eliminarAllByValor
from services.pedidoService import create, getAll, getAllByBuyer
main = Blueprint('pedidoRoute', __name__)

@main.route('/agregar', methods=['POST'])
@login_required
def generar():
    if current_user.rol == 'admin':
        return redirect(url_for('homrAdmin'))
    
    if request.method == 'POST':
        userName = current_user.nombre
        existe_carrito = obtenerValor(userName)
        if existe_carrito:
            pro = existe_carrito['productos']
            user = existe_carrito['usuario']
            montoTotal = existe_carrito['montoTotal']
            
            for producto in pro:
                nombre_producto = producto['nombre']
                producto_bd = getByName(nombre_producto)
                cantidad = int(producto_bd['cantidad'])
                if cantidad < 1:
                    eliminarAllByValor(userName)
                    return redirect(url_for('productoRoute.getAll'))

                resta = cantidad - 1
                update(producto_bd['id'],'sistema',None,None,None,str(resta))

            create(user, pro, float(montoTotal), userName, len(pro))
            eliminarAllByValor(userName)
            pedidos = getAllByBuyer(userName)
            return render_template('pedido/pedido.html', lista_pedidos=pedidos)
        else:
         return redirect(url_for('productoRoute.getAll'))
        
@main.route('/', methods=['GET'])
@login_required
def view():
    if current_user.rol == 'admin':
        return render_template('pedido/pedido.html', lista_pedidos=getAll())
    else:
        userName = current_user.nombre
        pedidos = getAllByBuyer(userName)
        return render_template('pedido/pedido.html', lista_pedidos=pedidos)
        