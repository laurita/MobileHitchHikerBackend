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
    g.t = storage.Trip(config.db_name)

@app.teardown_request
def teardown_request(req):
    if hasattr(g, 'j'):
        g.t.close()

@app.route('/')
def api_index():
    return 'Welcome to MobileHitchHiker Backend!'

@app.route('/trips')
def api_trips():
    if ('lat' in request.args) and ('long' in request.args):
        location = (float(request.args['lat']), float(request.args['long']),)
        if ('date' in request.args):
            date = request.args['date']
        else:
            date = 0
        data = g.t.find_closest(location, date)
    else:
        data = g.t.all()
    return Response(ser.trips(data), mimetype='application/json')

@app.route('/trips', methods=['POST'])
def api_store_trip():
    print request.json
    g.t.store(request.json)
    return 'ok'

if __name__ == '__main__':
    app.debug = True
    app.run()
