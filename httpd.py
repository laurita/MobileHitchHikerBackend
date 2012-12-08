from flask import Flask
from flask import Response
from flask import request
from flask import g
from flask import jsonify

import storage
import config
import serializer as ser

app = Flask(__name__)

@app.before_request
def before_request():
    g.j = storage.Journey(config.db_name)

@app.teardown_request
def teardown_request(req):
    if hasattr(g, 'j'):
        g.j.close()

@app.route('/')
def api_index():
    return 'Welcome to MobileHitchHiker Backend!'

@app.route('/journeys')
def api_journeys():
    if ('lat' in request.args) and ('long' in request.args):
        params = (float(request.args['lat']), float(request.args['long']),)
        data = g.j.find_closest(params)
    else:
        data = g.j.all()
    return Response(ser.journeys(data), mimetype='application/json')

@app.route('/journeys', methods=['POST'])
def api_store_journey():
    g.j.store(request.json)
    return 'ok'

if __name__ == '__main__':
    app.debug = True
    app.run()
