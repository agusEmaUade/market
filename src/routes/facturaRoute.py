from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import json

from services.pedidoService import getById, updatePedido
from services.facturaService import crearFactura, getAllByName, getFacturaAll
main = Blueprint('facturaRoute', __name__)

@main.route('/crear', methods=['POST'])
@login_required
def addFactura():
    if current_user.rol == 'admin':
        return redirect(url_for('homrAdmin'))
    
    if request.method == 'POST':
        userName = current_user.nombre
        pedido_id = request.form['pedido_id']
        metodo_pago = request.form['metodo_pago']

        existe_pedido = getById(pedido_id)
        if existe_pedido:
            crearFactura(existe_pedido, metodo_pago, userName)
            updatePedido(pedido_id, userName, 'facturado')
            facturas = getAllByName(userName)
            return render_template('factura/factura.html', lista_facturas=facturas)
        else:
         return redirect(url_for('productoRoute.getAll'))


@main.route('/', methods=['GET'])
@login_required
def view():
    if current_user.rol == 'admin':
        return render_template('factura/factura.html', lista_facturas=getFacturaAll())
    else:
        userName = current_user.nombre
        facturas = getAllByName(userName)
        return render_template('factura/factura.html', lista_facturas=facturas)