from flask import Flask
from backend.models import db,User
from backend.login import login_db
from backend.result import product_db
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_login import LoginManager

load_dotenv()

app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login_db.login'
app.register_blueprint(product_db)
app.register_blueprint(login_db)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

import backend.login
import backend.result
