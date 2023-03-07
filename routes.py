from app import app
from flask import Flask, render_template, url_for, request


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/add_vehicle')
def add_vehicle():
    return render_template('add_vehicle.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')