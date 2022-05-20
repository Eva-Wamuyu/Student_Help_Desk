from datetime import datetime
from flask import render_template,redirect,url_for,flash,session
from . import studentbp as student
from .forms import MakeRequest
from app.models import User,Request
from app import db
from flask_login import login_required
import jwt

@student.route('/')
#@login_required
def reqOpen():
  if confirmToken():
      print(confirmToken())
      user = confirmToken()
      studenti = User.query.filter_by(email=user['user']['email']).first()
      print(student)
      openReqs = Request.query.filter_by(student=studenti).filter_by(is_open=True).all()
      closedReqs = Request.query.filter_by(student=studenti).filter_by(is_open=False).all()
      return render_template("student/dashboard.html",openReqs=openReqs,closedReqs=closedReqs,student=studenti.name)
  return redirect(url_for("auth.login"))

@student.route("/mentors")
#@login_required
def main():
  if confirmToken():
      mentors = User.query.filter_by(role="Mentor").all()
      allMentors = User.query.filter_by(role="Mentor").all()
      req = Request.query.filter_by().all()
      #print(User.query.get(req[0].mentor_id).name)
      return render_template("student/mentors.html",mentors=mentors,reqs=req)
  return redirect(url_for('auth.login'))

@student.route("/query/<askwho>",methods=["GET", "POST"])
def queryfunc(askwho):
  if confirmToken():
    user = confirmToken()
    student = User.query.filter_by(email=user['user']['email']).first()
    form = MakeRequest()
    if form.validate_on_submit():
      mentor = User.query.filter_by(_id=askwho).first()
      #loginRequired Current user
     
      made_request = Request(form.message.data,True,datetime.now(),mentor,student)
      db.session.add(made_request)
      db.session.commit()
      flash("Message sent successfully")
      return redirect(url_for('.main'))

    return render_template("student/form.html",form=form)
  return redirect(url_for('auth.login'))

@student.route('/request/confirm')
def success():
  if confirmToken():
   return render_template("student/success.html")
  return redirect(url_for('.main'))


@student.route("/close/<id>")
#@login_required
def closeRequest(id):
  if confirmToken():
    if Request.query.get(id):
      requestQ = Request.query.get(id)
      if requestQ.is_open == True:
        requestQ.is_open = False
        db.session.add(requestQ)
        db.session.commit() 
      return redirect(url_for(".main"))
  return redirect(url_for('.main'))


def confirmToken():
  if 'jwt' in session:
    token = session['jwt']
    try:
      user = jwt.decode(token,key="hehe publik",algorithms="HS256")
    except Exception as e:
      return redirect(url_for('.app.login'))
    else:
      #if user.role == 'Student':
       return user
  return False