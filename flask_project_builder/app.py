from flask import Flask
from dynaconf import FlaskDynaconf


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app)
    app.config.load_extensions("EXTENSIONS")
    return app
