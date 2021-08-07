from datetime import datetime

import connexion
import pytest
from fitapi import create_app
from fitapi.models import Daily
from flask_sqlalchemy import SQLAlchemy


@pytest.fixture(scope='module')
def test_client():
    test_app = create_app(test=True)
 
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = test_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = test_app.app_context()
    ctx.push()
 
    yield testing_client  # this is where the testing happens!
 
    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    test_db = SQLAlchemy()
    test_db.create_all()
 
    # Insert Daily data
    day1 = Daily(startDate=datetime(1984, 1, 1), endDate=datetime(1984, 1, 2))
    day2 = Daily(startDate=datetime(1985, 1, 1), endDate=datetime(1985, 1, 2))
    test_db.session.add(day1)
    test_db.session.add(day2)
 
    # Commit the changes to db
    test_db.session.commit()
 
    yield test_db  # testing
 
    test_db.drop_all()

@pytest.fixture(scope='module')
def new_daily():
    daily = Daily(startDate=datetime(1984, 1, 1), endDate=datetime(1984, 1, 2))
    return daily

