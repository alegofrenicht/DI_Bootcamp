from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import datetime

app = Flask(__name__)

from config import Config

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from webapp import routes, models
