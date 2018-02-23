from flask import request
from flask import render_template
from flask import jsonify
from app import app
from .gmaps import GMaps
from .building import getBuilding
from .key import getKey

@app.route('/')
def home():
	return render_template('base.html')

@app.route('/map')
def mapdemo():
	return render_template('campusmap.html')
	
@app.route('/map', methods=['POST'])
def mapdemo_post():
	if request.method == 'POST':
		src = request.form['src1']
		cur = request.form['location']
	key = getKey()
	src = getBuilding(src)
	gmaps = GMaps(cur, src+", Fullerton")
	directions = gmaps.getDirections()
	tl = gmaps.getTripLength()
	if not src:
		return render_template('campusmap.html')
	else:
		return render_template('directions.html', src=src, directions=directions, tl=tl, key=key)

