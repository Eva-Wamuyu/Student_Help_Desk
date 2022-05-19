import datetime
from app.loginform import LoginForm
from flask import Flask,render_template,request,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from werkzeug.security import check_password_hash
import requests
from flask_login import login_user, logout_user, login_required, current_user,login_manager
from flask_bootstrap import Bootstrap
import jwt

#import request
db = SQLAlchemy()
bootstrap = Bootstrap()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'postgres://sycqczbabbwzls:12f6bc1d345e624ebf3698bbdf8c840cbb65b9a28d45c4614a738038ba9ea60b@ec2-54-86-224-85.compute-1.amazonaws.com:5432/d1kk9clmv4217h'
    db.init_app(app)
    bootstrap.init_app(app)
    # from .views import viewsc
    from .auth import auth as authbluep
    from .student import studentbp
    from .admin import adminbp
    from .mentor.views import mentorbp
    app.register_blueprint(studentbp, url_prefix="/student")
    app.register_blueprint(adminbp, url_prefix="/admin")
    app.register_blueprint(mentorbp, url_prefix="/mentor")
    app.register_blueprint(authbluep, url_prefix="/")
    from .models import User,Request
    #create_database(app)
    login_manager = LoginManager()
    #login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app







   
# def create_database(app):
#        if not path.exists("app/" + DB_NAME):
#         db.create_all(app=app)
#        print("Created database!")

    
#     @app.route('/',methods=['GET','POST'])
#     def login():
#         form = LoginForm()
#         email = request.form.get("email")
#         password = request.form.get("password")
#         print(form.validate_on_submit())
#         if form.validate_on_submit():
#             user = User.query.filter_by(email=email).first()
#             #print(check_password_hash(user.passwd,password))
#             if user is not None and check_password_hash(user.passwd,password):
#                 print("pass")
#                 # check_password_hash(user.passwd,password)
#                 if user.role == 'Mentor':
#                    register_session(form.email.data)
                    
#                    #login_user(user)
#                    login_manager.login_view = "mentorbp"
#                    login_manager.login_view = "mentorbp.views"
#                    return redirect(url_for("mentorbp.ProblemRequests",theirNum=user._id))
                        
#                 elif user.role == 'Admin':
#                     register_session(form.email.data)
#                     login_manager.login_view = "admin.views"
#                     return redirect(url_for("adminbp.home"))
#                 elif user.role == "Student":
#                     register_session(form.email.data)
#                     #login_user(user) 
#                     login_manager.login_view = "studentbp.views"
#                     return redirect(url_for("studentbp.reqOpen"))
                   
#                      #login_manager.login_view = "studentbp.views"
#                     print("here")
                    

#                 print(user.role)
#                 #flash("email or password is invalid")   
#         return render_template('admin/login.html',login_form=form)

#     def logout():
#         logout_user()
#         return redirect(url_for('login'))

      
    
        
     
   
    
        
        
        

      


      #return app
    # def create_database(app):
    #    if not path.exists("app/" + DB_NAME):
    #     db.create_all(app=app)
    #    print("Created database!")

# def register_session(themail):
#         user = {'email': themail}
#         time = int(datetime.datetime.now().timestamp())+172800
#         jwt_token = jwt.encode({'user':user,'exp':time},key="hehe publik",algorithm="HS256")
#         session['jwt'] = jwt_token





# ###################DB CONCEPTS HERE
# with app.app_context():
#       #db.create_all()
#       new_person = User.query.filter_by(_id=1).first()
#       new_person2 = User.query.filter_by(_id=2).first()
#       new_person3 = User.query.filter_by(role="Student").first()
#       new_person4 = User.query.filter_by(_id=1).first()
#       # new_person2 = User("hello2@gmail.com","hello2","",True,"Mentor","none","Android")
#       # new_person3 = User("hello33@gmail.com","hello33","",True,"Student","none","Android")
#       # new_person4 = User("hello@gmail.com","hello","",True,"Student","none","Fullstack")
#       newReq = Request("Help",True,datetime.today(),new_person,new_person3)
#       newReq2 = Request("Help",True,datetime.today(),new_person,new_person4)
#       newReq3 = Request("Help",True,datetime.today(),new_person,new_person4)
#       newReq4 = Request("Help",True,datetime.today(),new_person2,new_person3)
#       #db.session.add([new_person,new_person2,new_person3,new_person4])
#       db.session.add(newReq4)
#       db.session.commit()
#       #db.session.add([newReq,newReq2,newReq3,newReq4])