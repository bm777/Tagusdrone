from app import app
from flask import render_template
from app.db import Connexion


@app.route('/tables')
def tables():
	c = Connexion()
	c.create_connection()
	data = c.select_product()

	return render_template('tables.html', data=data)
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')