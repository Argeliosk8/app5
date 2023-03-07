from app import app
from flask import Flask, render_template, url_for, request, redirect, flash
from forms import RegistrationForm, LoginForm
from models import *
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return "Sorry you must be logged in to view this page"


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
    return render_template('login.html', form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for sigining up, welcome to Gas Tracker!')
        return redirect(url_for('login'))
    else:
        flash('error')
    return render_template('register.html', form = form)

@app.route('/add_vehicle')
def add_vehicle():
    return render_template('add_vehicle.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

