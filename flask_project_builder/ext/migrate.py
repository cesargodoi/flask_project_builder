from flask_migrate import Migrate

from flask_project_builder.ext.db import db
from flask_project_builder.ext.auth import models  # noqa
# import all the project models here

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)