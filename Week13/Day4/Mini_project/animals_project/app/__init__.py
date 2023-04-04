import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flask_app = Flask(__name__)

flask_app.config['SECRET_KEY'] = '123455'
flask_app.config['DEBUG'] = True
basedir = os.path.abspath(os.path.dirname(__file__))
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'petstore.db')
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from app import models, routes




