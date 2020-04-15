from app import app
from flask import render_template
from app.db import Connection

@app.route('/')
@app.route('/tables')
def index():
	c = Connection()
	c.conn()
	data = c.select_all()
	return render_template('tables.html', data=data)