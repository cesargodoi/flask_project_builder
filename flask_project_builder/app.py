from flask import Flask
from flask_project_builder.ext import config


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    return app