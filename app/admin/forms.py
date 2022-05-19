from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField,PasswordField,StringField
from wtforms.validators import DataRequired,Email


class LoginForm(FlaskForm):
  email = StringField("Email Address", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])


  
# class ProfilePhoto(FlaskForm):
#     img = 
