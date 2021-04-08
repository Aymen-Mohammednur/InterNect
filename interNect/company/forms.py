from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import  StringField,PasswordField,SubmitField,BooleanField,SelectField,TextAreaField
from wtforms.validators import DataRequired,EqualTo,Length,Email,email_validator,ValidationError


class CompanyRegistrationForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired(), 
                                            Length(min=2, max=35)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    street_address = StringField('Street Address', validators=[DataRequired(), 
                                            Length(min=2, max=25)])
    postal_code = StringField('Postal Code (Optional)')
    description = TextAreaField('Company Description (Optional)')
    category = SelectField('Class',  choices = [('Tech', 'Technology'), ('Constr', 'Construction'), ('Agro', 'Agriculture'), ('Bio', 'Biomedical'), ('Chem', 'Chemical'), ('Mechatro', 'Mechatronix')], validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                            validators=[DataRequired(),
                            EqualTo('password')])
    register = SubmitField('Register')

    def validate_email(self, email):
        email = False
        # Intern.query.filterby(email = email.data).first()

        if email:
            raise ValidationError("That email is already in use. Please choose another one.")

