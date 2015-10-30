__author__ = 'shafi'

import logging
import json
import os

from flask import Flask, url_for, request,render_template
from flask import Response
from flask import jsonify

app = Flask(__name__)

def check_auth(username, password):
    return username == 'admin' and password == 'password'

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Are you Sure ? if No Click cancel"'
    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/api/help', methods = ['GET'])
def help():
    '''Print available functions as json.'''
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)

@app.route('/hello', methods = ['GET'])
def api_hello():
    '''Print available functions.'''
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/info', methods = ['GET'])
def info():
    return open('sample.json').read()

@app.route('/restart', methods = ['GET'])
def restart():
    cmd = 'touch /tmp/sample.txt'
    os.popen(cmd)
    return "Succes"

@app.route('/regions', methods = ['GET'])
def demo5():
    '''Print available functions.'''
    cmd = 'aws ec2 describe-regions'
    running = os.popen(cmd)
    op = json.load(running)
    return render_template('index.html', res=op)

if __name__ == '__main__':
    file_handler = logging.FileHandler('/tmp/app.log')
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.run(debug=True, port=5000)