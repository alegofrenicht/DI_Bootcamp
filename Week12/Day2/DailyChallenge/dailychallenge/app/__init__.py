from flask import Flask
from DI_Bootcamp.Week12.Day2.DailyChallenge.dailychallenge import config

app = Flask(__name__)
app.config.from_object(config.Config)

from DI_Bootcamp.Week12.Day2.DailyChallenge.dailychallenge.app import routes
