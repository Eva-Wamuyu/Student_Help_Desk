from flask import Blueprint,render_template,redirect,url_for,session,request
from app.models import User
from werkzeug.security import check_password_hash
import jwt
import datetime

from . import auth


@auth.route('/',methods=['GET','POST'])
def login():
        form = LoginForm()
        email = request.form.get("email")
        password = request.form.get("password")
        print(form.validate_on_submit())
        if form.validate_on_submit():
            user = User.query.filter_by(email=email).first()
            #print(check_password_hash(user.passwd,password))
            if user is not None and check_password_hash(user.passwd,password):
                print("pass")
                # check_password_hash(user.passwd,password)
                if user.role == 'Mentor':
                   register_session(form.email.data)
                   return redirect(url_for("mentorbp.ProblemRequests",theirNum=user._id))
                        
                elif user.role == 'Admin':
                    register_session(form.email.data)
                    return redirect(url_for("adminbp.home"))
                elif user.role == "Student":
                    register_session(form.email.data)
                    #login_user(user) 
                    return redirect(url_for("studentbp.reqOpen"))
                   
                     #login_manager.login_view = "studentbp.views"
                    print("here")
                    

                print(user.role)
                #flash("email or password is invalid")   
        return render_template('admin/login.html',login_form=form)



from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField,PasswordField,StringField,BooleanField
from wtforms.validators import DataRequired,Email


class LoginForm(FlaskForm):
  email = StringField("Email Address", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  remember = BooleanField("Remember me")
  submit = SubmitField("Login", validators=[DataRequired()])


    
        
     
   
    
        
        
        

      


  
# def create_database(app):
#     if not path.exists("website/" + DB_NAME):
#         db.create_all(app=app)
#         print("Created database!")

def register_session(themail):
        user = {'email': themail}
        time = int(datetime.datetime.now().timestamp())+172800
        jwt_token = jwt.encode({'user':user,'exp':time},key="hehe publik",algorithm="HS256")
        session['jwt'] = jwt_token





#############