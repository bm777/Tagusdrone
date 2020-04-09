from app import app
from flask import render_template
from db import Connection

@app.route('/')
@app.route('/index')
def index():
	c = Connection()
	data = c.select_all()
	return render_template('index.html', data=data)