from flask import Flask, render_template
from dotenv import load_dotenv
import os

from repositories.mongo import mongo
from routes.producto import producto

config = load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)



app.register_blueprint(producto, url_prefix='/producto')

if __name__ == '__main__':
  app.run(debug=True, port=3000)