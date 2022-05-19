from . import adminbp
from flask import Blueprint, render_template, request, flash, redirect, url_for,request,session
from flask_login import login_required, current_user
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import requests
from sqlalchemy import text
import jwt
import datetime


@adminbp.route('/home')
def home():
    if confirmToken():
        student_count = User.query.filter(User.role == 'Student').count()
        mentor_count = User.query.filter(User.role == 'Mentor').count()

        sql = text("select role from user")
        result = db.engine.execute(sql)
        roles = [row[0] for row in result]
        print (roles)
        return render_template('admin/dashboard.html', students = student_count, mentors = mentor_count)
    
    return redirect(url_for('.adminlogin'))


@adminbp.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if confirmToken():
            user = confirmToken()
            print(user)
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
                    new_user = User(email=email, name=name,role=role,photo="none",stack=stack,is_present=True,passwd=generate_password_hash(password1, method='sha256'))
                    db.session.add(new_user)
                    db.session.commit()
                    # login_user(new_user, remember=True)
                    flash('User created!')
                    return redirect(url_for('.home'))

            return render_template("admin/signup.html", user=current_user)
    return redirect(url_for('.adminlogin'))

@adminbp.route("/logout")

def logout():
    
    return redirect(url_for("('.adminlogin"))



@adminbp.route('/', methods=['GET','POST'])
def adminlogin():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "studenthelp@admin.com" and login_form.password.data == "1234":
            user = {
                "email": "studenthelp@admin.com",
                "password": "1234"
            }        
            time = int(datetime.datetime.now().timestamp())+172800
            jwt_token = jwt.encode({'user':user,'exp':time},key="hehe publik",algorithm="HS256")
            session['jwt'] = jwt_token
            print(jwt_token)

        #user = "studenthelp@admin.login" and password = "4321"
        #user = User.query.filter_by(email = login_form.email.data).first()
        #if user is not None and user.passwd(login_form.password.data):
            #login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('adminbp.home'))
        flash('Invalid username or Password')
    return render_template('admin/login.html',login_form = login_form)




from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField,PasswordField,StringField,BooleanField
from wtforms.validators import DataRequired,Email


class LoginForm(FlaskForm):
  email = StringField("Email Address", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  remember = BooleanField("Remember me")
  submit = SubmitField("Login", validators=[DataRequired()])






def confirmToken():
  if 'jwt' in session:
    token = session['jwt']
    try:
      user = jwt.decode(token,key="hehe publik",algorithms="HS256")
    except Exception as e:
      return redirect(url_for('.adminlogin'))
    else:
      return user
  return False
# class ProfilePhoto(FlaskForm):
#     img = 




















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




@adminbp.route('/home')
def students():
    if confirmToken():
        student_count = User.query.filter(User.role == 'Student').all()
        return render_template('admin/data.html', items = student_count, header="All students")
    return redirect(url_for('.adminlogin'))

@adminbp.route('/mentors')
def mentors():
    if confirmToken():
        mentor_count = User.query.filter(User.role == 'Mentor').all()
        return render_template('admin/data.html',items = mentor_count,header="All Mentors")
    return redirect(url_for('.adminlogin'))

@adminbp.route("/purge/<num>")
def delete(num):
  if confirmToken():
    human = User.query.get(num)
    db.session.delete(human)
    db.session.commit()
    if human.role == "Mentor":
        return redirect(url_for('.mentors'))
    return redirect(url_for('.students'))
  return redirect(url_for('.adminlogin'))
  
