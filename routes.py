from app import app
from flask import Flask, render_template, url_for, request


@app.route('/login')
def login():
    return render_template('login.html')