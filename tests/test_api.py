import pytest
import connexion
from fitapi.models import Daily
from datetime import datetime


def test_swagger_ui_url(test_client):
    response = test_client.get("/api/ui/")
    assert response.status_code == 200


def test_daily_url(test_client):
    response = test_client.get("/api/daily")
    assert response.status_code == 200


def test_daily_model(new_daily):
    assert str(new_daily.startDate) == "1984-01-01 00:00:00"
    assert str(new_daily.endDate) == "1984-01-02 00:00:00"

def test_dates_url(test_client):
    response = test_client.get("/api/dates")
    assert response.status_code == 200

def test_one_user_one_date_url(test_client):
    response = test_client.get("/api/daily/2/date/01-01-1984")
    assert response.status_code == 200


def test_user_model(new_user):
    assert str(new_user.fname) == "Tony"
    assert str(new_user.lname) == "Stark"


def test_get_all_users_and_ordering_by_lname(test_client):
    url = "/api/daily"

    expected_json = [
        {'dates': [{'endDate': '1984-01-02 00:00:00','startDate': '1984-01-01 00:00:00','user_id': 2}],'fname': 'Tony','lname': 'Stark','user_id': 2},{'dates': [], 'fname': 'Lucas', 'lname': 'Stone-Drake', 'user_id': 1}
    ]
    response = test_client.get(url)
    assert response.json == expected_json


def test_get_one_valid_user(test_client):
    response = test_client.get("/api/daily/1")
    assert response.status_code == 200
    expected_json = {
'dates': [], 'fname': 'Lucas', 'lname': 'Stone-Drake', 'user_id': 1
    }
    assert response.json == expected_json


def test_get_one_invalid_user(test_client):
    response = test_client.get("/api/daily/15")
    assert response.status_code == 404

def test_get_all_dates_and_ordering_by_startdate(test_client):
    url = "/api/dates"

    expected_json = [
        {'endDate': '1985-01-02T00:00:00','startDate': '1985-01-01T00:00:00','user': None}, {'endDate': '1984-01-02T00:00:00','startDate': '1984-01-01T00:00:00','user': {'fname': 'Tony', 'lname': 'Stark', 'user_id': 2}}
    ]
    response = test_client.get(url)
    assert response.json == expected_json
