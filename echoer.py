import platform
import datetime

from flask import Flask, request, jsonify, g
from redis import Redis

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


def redis_db():
    db = Redis(host='redis', port=6379, db=0)
    return db


@app.before_request
def connect_db():
    if 'db' not in g:
        g.db = redis_db()


@app.after_request
def increment_counter(response):
    g.db.incr('count')

    return response


@app.route('/')
@app.route('/health', methods=['GET', 'POST', 'PUT'])
def echo():
    app.logger.info('logging info')

    status_code = request.args.get('status') or 200
    status_code = int(status_code)

    data = {
        'success': True,
        'status': status_code,
        'url': request.url,
        'base_url': request.base_url,
        'url_root': request.url_root,
        'method': request.method,
        'data': request.data.decode(encoding='UTF-8'),
        'date': datetime.datetime.now(),
        'host': request.host,
        'args': request.args,
        'form': request.form,
        'json': request.json,
        'cookies': request.cookies,
        'platform': platform.platform(),
        'node': platform.node(),
    }

    if 'headers' in request.args:
        data['headers'] = dict(request.headers)

    data['counter'] = int(g.db.get('count') or 0)
    return jsonify(data)


def main():
    app.run(port=8080, host='0.0.0.0')


if __name__ == "__main__":
    app.run()
