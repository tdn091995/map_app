from flask import request
from flask import render_template
from flask import jsonify
from app import app
from .gmaps import GMaps
from .forms import WebForm

@app.route('/')
def test():
	return render_template('index.html')
                           	
@app.route('/', methods=['POST'])
def test_post():
	if request.method == 'POST':
		src1 = request.form['src1']
		src2 = request.form['src2']
	gmaps = GMaps(src1, src2)	
	directions = gmaps.getDirections()
	if not directions:
		return render_template('empty.html')
	else:
		return render_template('gmaps.html', directions=directions)
		
@app.route('/mapdemo')
def mapdemo():
	return render_template('campusmap.html')
	
@app.route('/mapdemo', methods=['POST'])
def mapdemo_post():
	if request.method == 'POST':
		src = request.form['src1']
		cur = request.form['location']
		gmaps = GMaps(cur, src)
	directions = gmaps.getDirections()
	tl = gmaps.getTripLength()
	return render_template('directions.html', src=src, coord=cur, directions=directions, tl = tl)

