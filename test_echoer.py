import pytest
import fakeredis
from contextlib import contextmanager
from flask import appcontext_pushed, g, json
from echoer import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


@contextmanager
def redis_test(app):
    def handler(sender, **kwargs):
        g.db = fakeredis.FakeStrictRedis()
    with appcontext_pushed.connected_to(handler, app):
        yield


def test_response_200(client):
    with redis_test(app):
        with app.test_request_context('/'):
            g.db.incr('count')

            rv = client.get('/')
            assert rv.status_code == 200


def test_response_counter_increments(client):
    with redis_test(app):
        with app.test_request_context('/'):
            g.db.incr('count')

            rv = client.get('/')
            assert json.loads(rv.data)['counter'] == 1
            rv = client.get('/')
            assert json.loads(rv.data)['counter'] == 2
