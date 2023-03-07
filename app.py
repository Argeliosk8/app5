from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def index():
    return redirect(url_for('login'))

import routes