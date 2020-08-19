from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_project_builder.ext.db import db

from flask_project_builder.ext.auth.models import User
from flask_project_builder.ext.auth.admin import UserAdmin

admin = Admin()
def init_app(app):
    admin.name = 'FLASK_PROJECT_BUILDER'
    admin.template_mode = 'bootstrap3'
    admin.init_app(app)
    # here you will add other views to the admin
    admin.add_view(UserAdmin(User, db.session))
    # UserAdmin inherits from ModelView