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
	src = getBuilding(src)
	if(src == 'Pollak Library'):
		newSrc = '33.881530, -117.885766'
	elif(src == 'Computer Science Building'):
		newSrc = '33.882148, -117.882660'

	elif(src == 'Mihaylo'):
		newSrc = '33.878866, -117.883385'

	elif(src == 'McCarthy Hall'):
		newSrc = '33.879864, -117.885550'

	elif(src == 'Engineering Building'):
		newSrc = '33.882177, -117.883186'

	elif(src == 'Humanities-Social Sciences'):
		newSrc = '33.880497, -117.884462'

	elif(src == 'Kinesiology & Health Science'):
		newSrc = '33.882628, -117.885890'
	#gmaps = GMaps(cur, src+", Fullerton")#breaks cs and khs
	gmaps = GMaps(cur, newSrc)
	directions = gmaps.getDirections()
	tl = gmaps.getTripLength()
	if not src:
		return render_template('campusmap.html')
	else:
		return render_template('directions.html', src=src, directions=directions, tl=tl, key=key)
