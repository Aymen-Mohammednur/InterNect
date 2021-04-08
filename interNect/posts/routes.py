from flask import (Blueprint, render_template,url_for,
                    flash,redirect,request,abort,jsonify)
# from flask_login import current_user,login_required,current_user
from interNect import db
from flask_login import current_user,login_required
from interNect.posts.forms import PostForm

# import models here 
# import forms here





posts=Blueprint('posts',__name__)

@posts.route('/post',methods=['GET','POST'] )
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        post = Post(title=form.title.data, content=form.content.data, company_id=current_user.id)
    
        db.session.add(post)
        db.session.commit()

        flash(f'Company post has been posted.')
        return redirect(url_for('main.home'))

    return render_template('post.html',form=form)