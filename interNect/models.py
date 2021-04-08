from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from interNect import db
from flask_login import UserMixin

# Company - Name, email, Contact Info(address, phone, postal code), category

class Company(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String,unique=True, nullable=False )
    email = db.Column(db.String, unique=True, nullable=False)
    profile_img = db.Column(db.String, default='company.jpg',unique=False)
    password = db.Column(db.String(60),nullable=False)
    street_address= db.Column(db.String)
    phone_number=db.Column(db.String)
    category = db.Column(db.String)
    description= db.Column(db.Text)
    postal_code = db.Column(db.String)

    posts = db.relationship('Post',backref='author',lazy=True)
    


    def __repr__(self):
        return f"company ({self.name}, {self.email}, {self.profile_img})"

# Intern Applicant - Name, Email, DOB, Gender, Contact Info, OPTIONAL (Description, School Name)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20),nullable=False)    
    lname = db.Column(db.String(20),nullable=False)    
    username = db.Column(db.String(20),unique=True,nullable=False)    
    email = db.Column(db.String(120),unique=True,nullable=False)    
    dob = db.Column(db.DateTime)
    gender = db.Column(db.String,nullable=False)
    phone= db.Column(db.String)
    description= db.Column(db.Text)
    profile_img = db.Column(db.String(20),default='user.jpg')
    password = db.Column(db.String(60),nullable=False)


    applied = db.relationship('Pending',backref='user',lazy=True, foreign_keys='Pending.user_id')

    def __repr__(self):
        return f'User ({self.username},{self.email}, {self.profile_img})'    


# Post - Title, author (back ref), Content
class Post(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default =datetime.utcnow)
    content= db.Column(db.Text, nullable=False)
    company_id= db.Column(db.Integer, db.ForeignKey('company.id'),nullable=False)

    
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# Pending 
class Pending(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
