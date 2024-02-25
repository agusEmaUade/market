from flask import Flask, render_template, flash, redirect, url_for
from dotenv import load_dotenv
import os
from flask_login import LoginManager, login_required, logout_user, current_user

from repositories.mongo import mongo
from routes import loginRoute, productoRoute
from models.usuario import Usuario

config = load_dotenv()

app = Flask(__name__)

#set manager login
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
login_manager = LoginManager(app)

#set conexion mongo
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)



#route generales
@login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(mongo, user_id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Se ha cerrado sesión correctamente.', 'success')
    return redirect(url_for('index'))


#config module route
app.register_blueprint(productoRoute.main, url_prefix='/producto')
app.register_blueprint(loginRoute.main, url_prefix='/usuario')

if __name__ == '__main__':
  app.run(debug=True, port=3000)