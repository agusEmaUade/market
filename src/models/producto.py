class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'descripcion': self.descripcion
        }
    
    def to_dictFromBd(self):
        return {
            'id': str(self.id),
            'nombre': self.nombre,
            'precio': self.precio,
            'descripcion': self.descripcion
        }
    
    def from_mongo(doc):
        producto = Producto(doc['nombre'], doc['precio'], doc['descripcion'])
        producto.id= doc['_id']
        return producto