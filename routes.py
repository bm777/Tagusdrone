from . import *
from flask import render_template
from .db import Connexion


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

@app.route('/proformat')
def proformat():
	return render_template('proformat.html')