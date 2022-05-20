from . import adminbp
from flask import Blueprint, render_template, request, flash, redirect, url_for,request
from flask_login import login_required, current_user
from ..models import User
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import requests 


@adminbp.route('/')
def admin():
    
    return render_template('admin/dashboard.html')



@adminbp.route('/admin')
def dashboard():
    
    return render_template('admin/dashboard.html')

@adminbp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('app.admin'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("admin/login.html", user=current_user)


@adminbp.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        stack = request.form.get("stack")
        is_present = request.form.get("is_present")
        name = request.form.get("username")
        role = request.form.get("role")
        photo = request.form.get("photo")

        email_exists = User.query.filter_by(email=email).first()
        name_exists = User.query.filter_by(name=name).first()

        if email_exists:
            flash('Email is already in use.', category='error')
        elif name_exists:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Password don\'t match!', category='error')
        # elif len(username) < 2:
        #     flash('Username is too short.', category='error')
        elif len(password1) < 3:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            new_user = User(email=email, name=name,role=role,photo=photo,stack=stack,is_present=True,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('views.admin'))

    return render_template("admin/signup.html", user=current_user)


@adminbp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))



