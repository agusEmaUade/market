import json

from repositories.redis import conexion_redis



    
def guardarValor(clave, valor):
    # Convertir el valor a JSON antes de almacenarlo en Redis
    valor_json = json.dumps(valor)
    conexion_redis.get_redis_instance().set(clave, valor_json, 86400)

def guardarInformacionProducto(nombre_usuario, usuario, producto):
    # Verificar si ya existe información para el usuario
    info_usuario_json = conexion_redis.get_redis_instance().get(nombre_usuario)
    producto.fecha_creacion = None
    producto.fecha_actualizacion = None
    usuario.fecha_creacion = None
    usuario.fecha_actualizacion = None
    if not info_usuario_json:
        # Si no hay información para el usuario, guardarla por primera vez
        # Crear un diccionario con la información del usuario y el primer producto
        info_usuario = {
            'usuario': usuario.to_dict(),
            'productos': [producto.to_dict()],
            'montoTotal': producto.precio
        }
    else:
        # Si ya existe información, decodificarla de JSON a un diccionario
        info_usuario = json.loads(info_usuario_json)

        # Agregar el nuevo producto a la lista de productos
        info_usuario['productos'].append(producto.to_dict())

        # Actualizar el monto total sumando el precio del nuevo producto
        montoTotalFormat = float(info_usuario['montoTotal'])
        precioFormat = float( producto.precio)
        suma = montoTotalFormat + precioFormat
        info_usuario['montoTotal'] = str(suma)

    # Convertir el diccionario actualizado a JSON
    info_usuario_json = json.dumps(info_usuario)

    # Guardar la información en Redis
    conexion_redis.get_redis_instance().set(nombre_usuario, info_usuario_json, 180)

def obtenerValor(nombre_usuario):
    # Obtener la información de Redis en formato JSON
    info_usuario_json = conexion_redis.get_redis_instance().get(nombre_usuario)

    if info_usuario_json:
        # Si se encontró información, decodificarla de JSON a un diccionario
        return json.loads(info_usuario_json)
    else:
        return None

def eliminarInformacionProducto(nombre_usuario, producto):
    # Verificar si ya existe información para el usuario
    info_usuario_json = conexion_redis.get_redis_instance().get(nombre_usuario)
    if info_usuario_json:
        # Decodificar la información del usuario de JSON a un diccionario
        info_usuario = json.loads(info_usuario_json)

        # Obtener la lista de productos del usuario
        productos = info_usuario.get('productos', [])

        # Iterar sobre la lista de productos
        for index, prod in enumerate(productos):
            # Verificar si el producto actual coincide con el parámetro
            if prod.get('nombre') == producto.get('nombre'):
                # Eliminar el producto de la lista
                del productos[index]
                # Actualizar el monto total restando el precio del producto eliminado
                montoTotalFormat = float(info_usuario['montoTotal'])
                precioFormat = float(prod['precio'])
                resta = montoTotalFormat - precioFormat
                info_usuario['montoTotal'] = str(resta)
                break  # Salir del bucle una vez que se elimine el primer producto coincidente

        # Convertir el diccionario actualizado a JSON
        info_usuario_json = json.dumps(info_usuario)

        # Guardar la información actualizada en Redis
        conexion_redis.get_redis_instance().set(nombre_usuario, info_usuario_json, 180)


def eliminarAllByValor(clave):
    conexion_redis.get_redis_instance().delete(clave)
