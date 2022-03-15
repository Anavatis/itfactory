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

    app.register_blueprint(store)