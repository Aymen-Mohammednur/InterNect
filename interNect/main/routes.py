import os
import secrets
from PIL import Image
from flask import Blueprint,render_template,request,flash,redirect,url_for,request
from interNect import bcrypt
# import models here
from interNect.models import User,Company
# import forms here
from interNect.main.forms import LoginForm
from interNect.posts.forms import PostForm
from flask_login import login_user,logout_user
from interNect.intern.forms import InternUpdateForm
from interNect.models import Post
from flask_login import login_user, logout_user, current_user, login_required

main=Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html',posts=posts)


@main.route("/about")
def about():
    return render_template('about.html')
@main.route("/login",methods=["POST","GET"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        intern=User.query.filter_by(email=form.email.data).first()

        if (intern and bcrypt.check_password_hash(intern.password,form.password.data)):
            login_user(intern,remember=form.remember.data)
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))

            flash(f'Account created for {form.email.data}!', 'success')
        else:
            flash(f'Wrong email or password ' ,'danger')

        company=company.query.filter_by(email=form.email.data).first()

        if (company and            bcrypt.check_password_hash(company.password,form.password.data)):
            login_user(company,remember=form.remember.data)
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


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    
    output_size = (1215, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn

@main.route('/profile', methods=["POST","GET"])
@login_required
def profile():
    form = InternUpdateForm()
    if form.validate_on_submit():
        if form.profile_img.data:
            picture_file = save_picture(form.profile_img.data)
            current_user.profile_img = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profile'))

    elif request.method == 'GET':
        form.first_name.data = current_user.fname
        form.last_name.data = current_user.lname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.phone_number.data = current_user.phone
        form.description.data = current_user.description

    image = url_for('static', filename = 'profile_pics/' + current_user.profile_img)
    return render_template('intern_profile.html', title="Profile", image = image, form = form)