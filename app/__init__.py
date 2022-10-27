import os

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

from .auth import views


# Application factory function
def create_app() -> Flask:
    """
    Creates the Flask instance

    Return:
    app: Flask -> Flask instance
    """

    app: Flask = Flask(__name__,
                       template_folder='./templates',
                       static_folder='./static')
    bootstrap = Bootstrap5(app)

    app.config["SECRET_KEY"] = "SUPER_SECRET_KEY"

    # Configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    app.register_blueprint(views.auth)

    return app
