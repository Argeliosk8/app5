from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My_secret'
app.app_context().push()


@app.route('/')
@app.route('/home')
def index():
    return redirect(url_for('login'))

import routes