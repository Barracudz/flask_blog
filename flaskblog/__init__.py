from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f86503361e868a3ed9c2c76b0081d235'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # database
bcrypt = Bcrypt(app) # encryption
login_manager = LoginManager(app) # log in process
login_manager.login_view = 'login' # set default login page
login_manager.login_message_category = 'info'

from flaskblog import routes
