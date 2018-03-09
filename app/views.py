from flask import request
from flask import render_template
from flask import jsonify
from app import app
from .gmaps import GMaps
from .building import getBuilding
from .key import getKey

@app.route('/')
def home():
	key = getKey()
	return render_template('base.html', key=key)

@app.route('/map')
def mapdemo():
	key = getKey()
	return render_template('campusmap.html', key=key)
	
@app.route('/map', methods=['POST'])
def mapdemo_post():
	if request.method == 'POST':
		src = request.form['src1']
		cur = request.form['location']
	key = getKey()
	info = getBuilding(src)
	bld = info[0]
	coords = info[1]	
	gmaps = GMaps(cur, coords)
	directions = gmaps.getDirections()
	tl = gmaps.getTripLength()
	if not src:
		return render_template('campusmap.html')
	else:
		return render_template('directions.html', bld=bld, coords=coords, directions=directions, tl=tl, key=key)
