from flask import request_started,render_template
from flask import Blueprint
from app.models import Request, User

mentorbp = Blueprint("mentorbp",__name__,static_folder="./../static",template_folder="./../templates")


@mentorbp.route("/mentor")
def ProblemRequests():
    mentor = User.query.get(2)

    issue = Request.query.filter_by(mentor=mentor).all()
    print(issue)
    return render_template('mentor/dashboard.html', issue=issue)




    


