from flask import render_template, request
from app import app
from text_data import place_time

@app.route('/')
@app.route('/index.html')
def index():
	return render_template("index.html", place_time = place_time["1"], text = text["1"])
