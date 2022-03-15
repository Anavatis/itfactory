from dotenv import load_dotenv
from flask import Flask

from .database import db
load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)


def register_blueprints(app):

    from .store.views import store
    from .error.views import error
    from .admin.employee.views import admin_employee
    from .admin.store.views import admin_store
    from .admin.visit.views import admin_visit

    app.register_blueprint(store)
    app.register_blueprint(error)
    app.register_blueprint(admin_employee)
    app.register_blueprint(admin_store)
    app.register_blueprint(admin_visit)