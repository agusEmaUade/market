from flask import Blueprint, render_template, request, redirect, url_for
from services.productoService import get_todos_service


producto = Blueprint('producto', __name__)

@producto.route('/', methods=['GET'])
def getAll():
  # Mock de lista de productos (puedes reemplazar esto con tus datos reales)
    productos = [
        {"nombre": "Producto 1", "descripcion": "Descripción del Producto 1", "imagen": "pala.jpg", "precio": "$10.00"},
        {"nombre": "Producto 2", "descripcion": "Descripción del Producto 2", "imagen": "pala.jpg", "precio": "$15.00"},
        {"nombre": "Producto 3", "descripcion": "Descripción del Producto 3", "imagen": "pala.jpg", "precio": "$20.00"}
    ]

    pp = get_todos_service()
    print(pp)

    return render_template('index.html', productos=pp)

