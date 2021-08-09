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

        # Insert User data
        user1 = User(fname="Lucas", lname="Stone-Drake")
        user2 = User(fname="Tony", lname="Stark")
        db.session.add(user1)
        db.session.add(user2)

        # Insert Daily data
        day1 = Daily(startDate=datetime(1984, 1, 1), endDate=datetime(1984, 1, 2), user_id=user2.user_id)
        day2 = Daily(startDate=datetime(1985, 1, 1), endDate=datetime(1985, 1, 2), user_id=user2.user_id)
        db.session.add(day1)
        db.session.add(day2)

        user = User.query.filter_by(lname="Stark").first()
        user.dates = [day1]
    

        # Commit the changes to db
        db.session.commit()

    yield testing_client  # testing here

    ctx.pop()


@pytest.fixture(scope="module")
def new_daily():
    daily = Daily(startDate=datetime(1984, 1, 1), endDate=datetime(1984, 1, 2))
    return daily


@pytest.fixture(scope="module")
def new_user():
    user = User(fname="Tony", lname="Stark")
    day = Daily(startDate=datetime(1984, 1, 1), endDate=datetime(1984, 1, 2))
    user.dates = [day]
    return user
