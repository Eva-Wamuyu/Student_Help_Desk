from datetime import datetime
from flask import render_template,redirect,url_for,flash
from . import studentbp as student
from .forms import MakeRequest
from app.models import User,Request
from app import db
from flask_table import Table,Col
from flask_login import login_required

@student.route('/')
#@login_required
def reqOpen():
  student = User.query.get(3)
  print(student)
  openReqs = Request.query.filter_by(student=student).filter_by(is_open=True).all()
  closedReqs = Request.query.filter_by(student=student).filter_by(is_open=False).all()
  #print(Request.query.message)
  return render_template("student/dashboard.html",openReqs=openReqs,closedReqs=closedReqs)

@student.route("/mentors")
#@login_required
def main():
  mentors = User.query.filter_by(role="Mentor").all()
  allMentors = User.query.filter_by(role="Mentor").all()
  req = Request.query.filter_by(student_id = 3).all()
  print(User.query.get(req[0].mentor_id).name)
  return render_template("student/mentors.html",mentors=mentors,reqs=req)

@student.route("/query/<askwho>",methods=["GET", "POST"])
def queryfunc(askwho):
  form = MakeRequest()
  if form.validate_on_submit():
    mentor = User.query.filter_by(_id=askwho).first()
    #loginRequired Current user
    student = User.query.get(3)
    made_request = Request(form.message.data,True,datetime.now(),mentor,student)
    db.session.add(made_request)
    db.session.commit()
    flash("Message sent successfully")
    return redirect(url_for('.main'))

  return render_template("student/form.html",form=form)


@student.route('/request/confirm')
#@login_required
def success():
  return render_template("student/success.html")



@student.route("/close/<id>")
#@login_required
def closeRequest(id):
  requestQ = Request.query.get(id)
  if requestQ.is_open == True:
    requestQ.is_open = False
    db.session.add(requestQ)
    db.session.commit() 
  return redirect(url_for(".main"))



@student.route('/edit/<user>')
def edit_profile():
  # user = User.query.filter_by(_id=1).first()
  # form = User(user)
  return render_template("student/dashboard.html")

