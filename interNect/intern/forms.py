from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import  StringField,PasswordField,SubmitField,BooleanField,SelectField,TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,EqualTo,Length,Email,email_validator,ValidationError
from interNect.models import User

class InternRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), 
                                            Length(min=2, max=15)])
    last_name = StringField('Last Name', validators=[DataRequired(), 
                                            Length(min=2, max=15)])
    username = StringField('Username', validators=[DataRequired(), 
                                            Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = SelectField('Gender',  choices = [('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth')
    # , format='%m-%D-%Y'
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    description = TextAreaField('Description (Optional)')
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                            validators=[DataRequired(),
                            EqualTo('password')])
    register = SubmitField('Register')

    def validate_email(self, email):
        #email = False
        email = User.query.filter_by(email = email.data).first()

        if email:
            raise ValidationError("That email is already in use. Please choose another one.")




class InternUpdateForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), 
                                            Length(min=2, max=15)])
    last_name = StringField('Last Name', validators=[DataRequired(), 
                                            Length(min=2, max=15)])
    username = StringField('Username', validators=[DataRequired(), 
                                            Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = SelectField('Gender',  choices = [('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth')
    # , format='%m-%D-%Y'
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    description = StringField('Description (Optional)')
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    update = SubmitField('Update')

    def validate_email(self, email):
    
        # Intern.query.filterby(email = email.data).first()

        if email != self.email:
            raise ValidationError("Sorry Can't Change Email.")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError("That username is taken. Please choose a different one.")

    # def validate_email(self, email):
    #     if email.data != current_user.email:
    #         email = User.query.filter_by(email=email.data).first()

    #         if email:
    #             raise ValidationError("That email is taken. Please choose a different one.")

