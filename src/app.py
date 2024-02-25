from flask import Flask, render_template
from dotenv import load_dotenv
import os

from repositories.mongo import mongo
from routes import producto, loginRoute

config = load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)



app.register_blueprint(producto.main, url_prefix='/producto')
app.register_blueprint(loginRoute.main, url_prefix='/login')

if __name__ == '__main__':
  app.run(debug=True, port=3000)