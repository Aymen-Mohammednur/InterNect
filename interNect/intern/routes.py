from flask import (Blueprint, render_template,url_for,
                    flash,redirect,request,abort)
from interNect.intern.forms import InternRegistrationForm

from interNect import bcrypt,db


# import models here
# import forms here
# from flask_login import login_user,current_user,logout_user,login_required


from interNect import db,bcrypt
from interNect.models import User

intern=Blueprint('intern',__name__)

@intern.route('/InternRegister',methods=['GET','POST'] )
def InternRegister():
    form=InternRegistrationForm()
    print("\n\n\n here 1 \n\n\n")

    if form.validate_on_submit():
        print("\n\n\n here 2 \n\n\n")

        password=bcrypt.generate_password_hash(form.password.data).\
            decode('utf-8')
        intern=User(fname = form.first_name.data, 
                lname = form.last_name.data,
                 username = form.username.data, 
                 email = form.email.data,
                 gender = form.gender.data,
                 dob = form.date_of_birth.data,
                 phone = form.phone_number.data,
                 description = form.description.data,
                 password = password)
        print("\n\n\n here 3 \n\n\n")
        db.session.add(intern)
        db.session.commit()
        flash(f'Account has ben created for {form.first_name.data} {form.last_name.data}!', 'success')
        return redirect(url_for('main.login'))

    return render_template('intern_register.html',form=form)



 