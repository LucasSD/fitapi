import os

import connexion
from flask import Flask, render_template
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = connexion.App(__name__, specification_dir=basedir)

    # Read the swagger.yml file to configure the endpoints
    app.add_api("swagger.yml")

    app = app.app

    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        basedir, "daily.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Create the SQLAlchemy db instance
    db = SQLAlchemy(app)

    # Initialize Marshmallow
    ma = Marshmallow(app)

    @app.route("/")
    def home():
        """
        :return:        the rendered template 'home.html'
        """
        return render_template("home.html")

    return app
