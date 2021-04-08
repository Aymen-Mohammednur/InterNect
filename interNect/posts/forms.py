
    
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField,SubmitField
from wtforms.validators import DataRequired,Length
from flask_login import current_user



class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), 
                                            Length(min=2, max=20)])
    
    content = StringField('Content', validators=[DataRequired(), 
                                            Length(min=2, max=75)])

    post = SubmitField('Post')




class PostUpdateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), 
                                            Length(min=2, max=15)])
    
    content = StringField('Content', validators=[DataRequired(), 
                                            Length(min=2, max=15)])

    update = SubmitField('Update')

