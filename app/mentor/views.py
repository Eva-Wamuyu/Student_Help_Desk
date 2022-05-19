from flask import request_started,render_template, url_for,redirect
from flask import Blueprint
from app.models import Request, User
from app.student.views import confirmToken
from app import db
mentorbp = Blueprint("mentorbp",__name__)


@mentorbp.route("/")
def ProblemRequests():
    if confirmToken():
        
        getuser = confirmToken()
        mentor = User.query.filter_by(email=getuser['user']['email']).first()
        message = f"Hello {mentor.name} here are all blockers That are pending and addressed to you"
        issue = Request.query.filter_by(mentor=mentor).filter_by(is_open=True).all()
        print(issue)
        return render_template('mentor/dashboard.html', issue=issue,message=message)
    return redirect(url_for('auth.login'))

@mentorbp.route("/mentor/new")
def studentRequests():    
    student = User.query.get(3)
    req = Request.query.filter_by(student=student).all
    print(req)

@mentorbp.route("/closed")
def closed():
    if confirmToken():
        getuser = confirmToken()
        mentor = User.query.filter_by(email=getuser['user']['email']).first()
        message = f"These are the closed issues"
        #issue = Request.query.filter_by(mentor=mentor).all()
        issue = Request.query.filter_by(mentor_id=mentor._id).filter_by(is_open=False).all()
        #print(issue)
        return render_template('mentor/dashboard.html', issue=issue,message=message)
    return redirect(url_for('auth.login'))


@mentorbp.route("/open")
def open():
    if confirmToken():
        getuser = confirmToken()
        mentor = User.query.filter_by(email=getuser['user']['email']).first()
        issue = Request.query.filter_by(mentor_id=mentor._id).filter_by(is_open=True).all()
        #issue = Request.query.filter_by(mentor=mentor).all()
        #issue = Request.query.filter_by(mentor=mentor).filter_by(is_open=True).all()
        openReq = Request.query.filter_by(mentor=mentor).all()
        closedReqs = Request.query.filter_by(mentor=mentor).all()
        message = f"These are the open issues"
        #print(issue)
        return render_template('mentor/dashboard.html', issue=openReq,message=message)
    return redirect(url_for('auth.login'))

    #issue = Request.query.filter_by(mentor=mentor).filter_by(is_open=False).all()

@mentorbp.route("/close/<num>")
def closeRequest(num):
  if confirmToken():
    requestQ = Request.query.get(num)
    if requestQ.is_open == True:
      requestQ.is_open = False
      db.session.add(requestQ)
      db.session.commit()
    elif requestQ.is_open == False:
      requestQ.is_open = True
      db.session.add(requestQ)
      db.session.commit()
    return redirect(url_for(".ProblemRequests"))
  return redirect(url_for('.main'))


@mentorbp.route("/forward/", methods=['GET'])
def move_forward():
    if confirmToken():

        forward_message = "Show Request..."
        return render_template('/mentor/new.html', forward_message=forward_message);
    return redirect(url_for('auth.login'))

@mentorbp.route("/all")
def all():
    if confirmToken():
        getuser = confirmToken()
        mentor = User.query.filter_by(email=getuser['user']['email']).first()
        message = f"These are the closed issues"
        #issue = Request.query.filter_by(mentor=mentor).all()
        issue = Request.query.filter_by(mentor_id=mentor._id).all()
        #print(issue)
        return render_template('mentor/dashboard.html', issue=issue,message=message)
    return redirect(url_for('auth.login'))


