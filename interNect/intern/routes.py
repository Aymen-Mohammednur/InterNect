from flask import (Blueprint, render_template,url_for,
                    flash,redirect,request,abort)
from interNect.intern.forms import InternRegistrationForm

from interNect import bcrypt,db


# import models here
# import forms here
# from flask_login import login_user,current_user,logout_user,login_required




intern=Blueprint('intern',__name__)

@intern.route('/InternRegister',methods=['GET','POST'] )
def InternRegister():
    form=InternRegistrationForm()
    if form.validate_on_submit():
        print()
        print()
        print(form.first_name.data)
        print()
        print()
        flash(f'Account created for {form.first_name.data}!', 'success')

    return render_template('intern_register.html',form=form)



 