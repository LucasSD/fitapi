import pytest
import connexion
from fitapi.models import Daily
from datetime import datetime

def test_swagger_ui_url(test_client):
    response = test_client.get('/api/ui/')
    assert response.status_code == 200

def test_daily_url(test_client):
    response = test_client.get('/api/daily')
    assert response.status_code == 200

def test_daily_model(new_daily):
    assert str(new_daily.startDate) == '1984-01-01 00:00:00'
    assert str(new_daily.endDate) == '1984-01-02 00:00:00'

def test_get_all_daily(test_client):
    url = "/api/daily"
    expected_json = [{'day_id': None,'endDate': '1984-01-02T00:00:00','startDate': '1984-01-01T00:00:00'},{'day_id': None,'endDate': '1985-01-02T00:00:00','startDate': '1985-01-01T00:00:00'}]
    response = test_client.get(url)
    assert response.json == expected_json




