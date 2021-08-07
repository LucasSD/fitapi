import pytest
import connexion
from fitapi import app
from fitapi.models import Daily
from datetime import datetime

def test_swagger_ui_url(client):
    response = client.get('/api/ui/')
    assert response.status_code == 200

'''def test_daily_url(client):
    response = client.get('/api/daily')
    assert response.status_code == 200'''

def test_daily_model(new_daily):
    assert str(new_daily.startDate) == '1984-01-01 00:00:00'
    assert str(new_daily.endDate) == '1984-01-02 00:00:00'

'''def test_get_all_daily(client):
    url = "/api/daily"
    expected_json = []
    response = client.get(url)
    assert response.json == expected_json'''




