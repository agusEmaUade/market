from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(UserMixin):
    def __init__(self, username, password, email, rol='comprador', _id=None):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.email = email
        self.rol = rol
        self.id = _id

    def to_dict(self):
        return {
            '_id': str(self.id),
            'username': self.username,
            'password_hash': self.password_hash,
            'email': self.email,
            'rol': self.rol
        }

    def from_mongo(doc):
        return Usuario(doc['username'], doc['password_hash'], doc['email'], doc['rol'], doc['_id'])