from datetime import datetime

import connexion
import pytest
from fitapi import create_app
from fitapi.models import Daily, User
from flask_sqlalchemy import SQLAlchemy
from fitapi import db


@pytest.fixture(scope="module")
def test_client():
    test_app = create_app()

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = test_app.test_client()

    test_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    # Establish an application context before running the tests.
    ctx = test_app.app_context()
    ctx.push()
    with ctx:
        db.create_all()
        # Insert Daily data
        day1 = Daily(startDate=datetime(1984, 1, 1), endDate=datetime(1984, 1, 2))
        day2 = Daily(startDate=datetime(1985, 1, 1), endDate=datetime(1985, 1, 2))
        db.session.add(day2)
        db.session.add(day1)

        # Commit the changes to db
        db.session.commit()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope="module")
def new_daily():
    daily = Daily(startDate=datetime(1984, 1, 1), endDate=datetime(1984, 1, 2))
    return daily


@pytest.fixture(scope="module")
def new_user():
    user = User(fname="Tony", lname="Stark")
    return user
