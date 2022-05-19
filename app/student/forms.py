from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField,PasswordField
from wtforms.validators import DataRequired


class MakeRequest(FlaskForm):
  message = SelectField("The blocker you'd like to be addressed",choices=[("IP","IP"),("Content","content"),("Bugs","Bugs"),("other","other")])
  submit = SubmitField("send")

class StudentProfile(FlaskForm):
  passwd = PasswordField("Password to change",validators=[DataRequired()])
  newpasswd = PasswordField("New password",validators=[DataRequired()])
  newpasswd2 = PasswordField("Confirm password",validators=[DataRequired()])
  
# class ProfilePhoto(FlaskForm):
#     img = 
