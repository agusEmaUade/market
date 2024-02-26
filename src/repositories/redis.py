import redis
from dotenv import load_dotenv
import os

load_dotenv()

class ConexionRedis:
    def __init__(self, host='localhost', port=6379, password=None):
        self.host = host
        self.port = port
        self.password = password
        self.redis_instance = self.establecer_conexion()

    def establecer_conexion(self):
        return redis.Redis(host=self.host, port=self.port, password=self.password)

    def get_redis_instance(self):
        return self.redis_instance

# Crear una instancia de la clase para usarla en otros archivos
conexion_redis = ConexionRedis(
    host=os.getenv('REDIS_HOST'),
    port=int(os.getenv('REDIS_PORT')),
    password=os.getenv('REDIS_PASSWORD')
)