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


def test_user_model(new_user):
    assert str(new_user.fname) == "Tony"
    assert str(new_user.lname) == "Stark"


def test_get_all_daily_and_ordering(test_client):
    url = "/api/daily"

    # 1985 date was added to db first
    expected_json = [
        {"endDate": "1984-01-02T00:00:00", "startDate": "1984-01-01T00:00:00"},
        {"endDate": "1985-01-02T00:00:00", "startDate": "1985-01-01T00:00:00"},
    ]
    response = test_client.get(url)
    assert response.json == expected_json


def test_get_one_valid_daily(test_client):
    response = test_client.get("/api/daily/01-01-1984")
    assert response.status_code == 200
    expected_json = {
        "endDate": "1984-01-02T00:00:00",
        "startDate": "1984-01-01T00:00:00",
    }
    assert response.json == expected_json


def test_get_one_invalid_daily(test_client):
    response = test_client.get("/api/daily/01-01-2000")
    assert response.status_code == 404
