from flask import request_started,render_template
from flask import Blueprint
from app.models import Request, User

mentorbp = Blueprint("mentorbp",__name__,static_folder="./../static",template_folder="./../templates")


@mentorbp.route("/mentor")
def mentorLanding():
    mentor = User.query.get(2)
    student = User.query.get(3)
    print(student)
   
    req = Request.query.filter_by(mentor=mentor).all()
    print(req)
    return render_template('mentor/dashboard.html', req=req, student=student)
