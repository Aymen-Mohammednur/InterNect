from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import  StringField,PasswordField,SubmitField,BooleanField,SelectField
from wtforms.validators import DataRequired,EqualTo,Length,Email,email_validator,ValidationError


class LoginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=4)])
    remeber=BooleanField("Remeber Me")
    submit=SubmitField("Login")
   
    