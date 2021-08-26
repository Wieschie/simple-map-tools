from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import str
from builtins import int
from future import standard_library
standard_library.install_aliases()
import os.path
from flask import Flask, send_file, make_response
app = Flask(__name__)

mapTypes = ['bestAvailable', 'usgsHRO', 'usgsNAIP', 'indiana', 'osm']
default = '/data/default.png'

@app.route('/tiles/<mapType>/<zoom>/<x>/<y>', methods=['GET', 'POST'])
def tiles(mapType, zoom, x, y):
    # convert XYZ to TMS for necessary maps
    # if mapType in tmsMaps:
    #     y = TmsXyxSwap(zoom, y)
    if y.endswith('.png'):
        y = y[:-4]
    filename = GetTilePath(mapType, zoom, x, y)
    if mapType not in mapTypes or not os.path.isfile(filename):
        filename = default
    return send_file(filename)

def GetBestAvailable(zoom, x, y):
# this is prioritized by level of detail (high -> low)
    for t in mapTypes[1:]:
        filename = GetTilePath(t, zoom, x, y)
        if os.path.isfile(filename):
            return filename
    return default

def GetTilePath(mapType, zoom, x, y):
    if mapType == "bestAvailable":
         return GetBestAvailable(zoom, x, y)
    return f"/data/{mapType}/{zoom}/{x}/{y}.png"

@app.route('/')
def map():
    return send_file('/app/map.html')

@app.route('/leaflet/<resource>')
def leaflet(resource):
    return send_file(f"/app/leaflet/{resource}")

@app.route('/leaflet/images/<image>')
def leafletImage(image):
    return send_file(f"/app/leaflet/images/%{image}")

@app.route('/capabilities')
def capabilities():
    response = make_response(''.join([f"/tiles/{m}/{{z}}/{{x}}/{{y}}\n" for m in mapTypes]))
    response.headers["content-type"] = "text/plain"
    return response

def TmsXyxSwap(zoom, y):
    return str((2 ** int(zoom)) - int(y) - 1)

if __name__ == '__main__':
    app.run()