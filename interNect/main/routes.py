from flask import Blueprint,render_template,request,flash,redirect,url_for,request
from interNect import bcrypt
# import models here
from interNect.models import User,Company
# import forms here
from interNect.main.forms import LoginForm
from interNect.posts.forms import PostForm
from flask_login import login_user,logout_user


main=Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html')
@main.route("/login",methods=["POST","GET"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        intern=User.query.filter_by(email=form.email.data).first()

        if (intern and            bcrypt.check_password_hash(intern.password,form.password.data)):
            login_user(intern,remember=form.remember.data)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))

            flash(f'Account created for {form.email.data}!', 'success')
        else:
            flash(f'Wrong email or password ' ,'danger')

    
    return render_template('login.html',form=form,title="Login")

@main.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))




