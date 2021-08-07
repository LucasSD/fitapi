import pytest
import connexion
from fitapi.models import Daily
from datetime import datetime

def test_swagger_ui_url(test_client, init_database):
    response = test_client.get('/api/ui/')
    assert response.status_code == 200

def test_daily_url(test_client, init_database):
    response = test_client.get('/api/daily')
    assert response.status_code == 200

def test_daily_model(new_daily):
    assert str(new_daily.startDate) == '1984-01-01 00:00:00'
    assert str(new_daily.endDate) == '1984-01-02 00:00:00'

def test_get_all_daily(test_client, init_database):
    url = "/api/daily"
    expected_json = []
    response = test_client.get(url)
    assert response.json == expected_json




