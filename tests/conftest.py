import pytest
import connexion
from fitapi import app
from fitapi.models import Daily
from datetime import datetime

app.add_api('swagger.yml')

@pytest.fixture(scope='module')
def client():
    with app.app.test_client() as c:
        yield c

@pytest.fixture(scope='module')
def new_daily():
    daily = Daily(startDate=datetime(1984, 1, 1), endDate=datetime(1984, 1, 2))
    return daily

