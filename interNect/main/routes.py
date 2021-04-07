from flask import Blueprint,render_template,request,flash
# import models here
# import forms here
from interNect.main.forms import LoginForm


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

    if form.validate_on_submit:
        print()
        print()
        print(form.email.data)
        print()
        print()
        flash(f'Account created for {form.email.data}!', 'success')
    
    return render_template('login.html',form=form)




