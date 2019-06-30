from flask import Flask, request, jsonify
import platform

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def echo():

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
        'host': request.host,
        'args': request.args,
        'form': request.form,
        'json': request.json,
        'cookies': request.cookies,
        'platform': platform.platform(),
        'node': platform.node(),
    }

    return jsonify(data)

def main():
    app.run(port=8080, host='0.0.0.0')

if __name__ == "__main__":
    app.run()
