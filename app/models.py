from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
  _id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String,unique=True,nullable=False)
  name = db.Column(db.String,nullable=False)
  passwd = db.Column(db.String,nullable=False)
  is_present = db.Column(db.Boolean)
  role = db.Column(db.String,nullable=False)
  photo = db.Column(db.String)
  stack = db.Column(db.String,nullable=False)
  #request = db.relationship("Request",backref="user",lazy="dynamic")
  

  def __init__(self,email,name,passwd,is_present,role,photo,stack):
    self.email = email
    self.name = name
    self.passwd = generate_password_hash(passwd)
    self.is_present = is_present
    self.role = role
    self.photo = photo
    self.stack = stack





class Request(db.Model):
  _id = db.Column(db.Integer,primary_key=True)
  message = db.Column(db.String,nullable=False)
  time = db.Column(db.Date)
  is_open = db.Column(db.Boolean,default=True)
  mentor_id = db.Column(db.Integer, db.ForeignKey("user._id"),nullable=False)
  student_id = db.Column(db.Integer, db.ForeignKey("user._id"),nullable=False)
  mentor = db.relationship("User",foreign_keys=[mentor_id])
  student = db.relationship("User",foreign_keys=[student_id])
  

  def __init__(self,message,is_open,time,mentor,student):
    self.message = message
    self.is_open = is_open
    self.time = time
    self.mentor = mentor
    self.student = student
    