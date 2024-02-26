from datetime import datetime

class Factura:
    def __init__(self, pedido, forma_pago, usuario_actualizacion,estado="generada", fecha_creacion= datetime.now(), fecha_actualizacion= datetime.now()):
        self.pedido = pedido
        self.forma_pago = forma_pago
        self.estado = estado
        self.usuario_actualizacion = usuario_actualizacion
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion
       
       

    def to_dict(self):
        return {
            'pedido': self.pedido.to_dict(),
            'forma_pago': self.forma_pago,
            'estado': self.estado,
            'usuario_actualizacion': self.usuario_actualizacion,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion

        }
    
    def to_dictFromBd(self):
        return {
            'id': str(self.id),
            'pedido': self.pedido,
            'forma_pago': self.forma_pago,
            'estado': self.estado,
            'usuario_actualizacion': self.usuario_actualizacion,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion
        }
    
    def from_mongo(doc):
        factura = Factura(doc['pedido'], doc['forma_pago'], doc['usuario_actualizacion'], doc['estado'], doc['fecha_creacion'], doc['fecha_actualizacion'])
        factura.id= doc['_id']
        return factura