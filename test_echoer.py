import pytest
from echoer import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_response_200(client):
    rv = client.get('/')
    assert rv.status_code == 200
