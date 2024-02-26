from datetime import datetime

class Pedido:
    def __init__(self, usuario, productos, montoTotal, usuario_actualizacion, cantidadItem,estado="en-preparacion", fecha_creacion= datetime.now(), fecha_actualizacion= datetime.now()):
        self.usuario = usuario
        self.productos = productos
        self.montoTotal = montoTotal
        self.cantidadItem = cantidadItem
        self.estado = estado
        self.usuario_actualizacion= usuario_actualizacion
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion
       
       

    def to_dict(self):
        return {
            'usuario': self.usuario,
            'productos': self.productos,
            'montoTotal': self.montoTotal,
            'cantidadItem': self.cantidadItem,
            'estado': self.estado,
            'usuario_actualizacion': self.usuario_actualizacion,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion

        }
    
    def to_dictFromBd(self):
        return {
            'id': str(self.id),
            'usuario': self.usuario,
            'productos': self.productos,
            'montoTotal': self.montoTotal,
            'cantidadItem': self.cantidadItem,
            'estado': self.estado,
            'usuario_actualizacion': self.usuario_actualizacion,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion
        }
    
    def from_mongo(doc):
        pedido = Pedido(doc['usuario'], doc['productos'], doc['montoTotal'], doc['usuario_actualizacion'], doc['cantidadItem'], doc['estado'], doc['fecha_creacion'], doc['fecha_actualizacion'])
        pedido.id= doc['_id']
        return pedido