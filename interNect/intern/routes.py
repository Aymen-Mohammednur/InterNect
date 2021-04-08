from flask import (Blueprint, render_template,url_for,
                    flash,redirect,request,abort)
from interNect.intern.forms import InternRegistrationForm

from interNect import bcrypt,db


# import models here
# import forms here
# from flask_login import login_user,current_user,logout_user,login_required


from internect import db,bcrypt
from InterNect.models import User

intern=Blueprint('intern',__name__)

@intern.route('/InternRegister',methods=['GET','POST'] )
def InternRegister():
    form=InternRegistrationForm()
    if form.validate_on_submit():

        password=bcrypt.generate_password_hash(form.password.data).\
            decode('utf-8')
        intern=User(form.first)
        
        flash(f'Account created for {form.first_name.data}!', 'success')

    return render_template('intern_register.html',form=form)



 