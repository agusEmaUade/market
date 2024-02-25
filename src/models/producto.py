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
    
    def from_mongo(doc):
        return Producto(doc['nombre'], doc['precio'], doc['descripcion'])