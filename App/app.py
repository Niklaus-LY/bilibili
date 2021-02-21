# -*- coding:utf-8 -*-

from flask import Flask
from views.api import api_blueprint
from views.home import home_blueprint
from model.model import  db


app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
app.config.from_object("config")

app.register_blueprint(home_blueprint)
app.register_blueprint(api_blueprint)

db.init_app(app)
app.run()
