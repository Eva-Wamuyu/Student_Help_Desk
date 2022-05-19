from datetime import datetime
from xxlimited import new
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
# import request
db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'postgres://sycqczbabbwzls:12f6bc1d345e624ebf3698bbdf8c840cbb65b9a28d45c4614a738038ba9ea60b@ec2-54-86-224-85.compute-1.amazonaws.com:5432/d1kk9clmv4217h'
    db.init_app(app)
    # from .views import views
    #from .auth import auth
    #from student import studentbp
    # fromadmin import adminbp
    #from mentor import mentorbp
    # app.register_blueprint(studentbp, url_prefix="/")
    # app.register_blueprint(adminpb, url_prefix="/admin")
    # app.register_blueprint(mentorbp, url_prefix="/mentor")
    
    from .models import User,Request
    #create_database(app)
    #login_manager = LoginManager()
    #login_manager.login_view = "auth.login"
    #login_manager.init_app(app)
    #@login_manager.user_loader
    #def load_user(id):
        #return User.query.get(int(id))
    
    # REGITERING BLUEPRINTS
    from .admin import adminbp as admin_blueprint
    app.register_blueprint(admin_blueprint)




    return app
def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created database!")

      





###################DB CONCEPTS HERE
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