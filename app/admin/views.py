from . import adminbp 
from flask import Flask, render_template, url_for, flash, redirect
from ..models import  User, Request
from sqlalchemy import text
from .. import db
from .forms import LoginForm
from flask_login import login_user

@adminbp.route('/')
def home():
    student_count = User.query.filter(User.role == 'Student').count()
    mentor_count = User.query.filter(User.role == 'Mentor').count()

    sql = text("select role from user")
    result = db.engine.execute(sql)
    roles = [row[0] for row in result]
    print (roles)
    return render_template('admin/dashboard.html', students = student_count, mentors = mentor_count)

@adminbp.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.passwd(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('adminbp.home'))

        flash('Invalid username or Password')

    return render_template('admin/login.html',login_form = login_form)