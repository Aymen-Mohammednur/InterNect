from flask import (Blueprint, render_template,url_for,
                    flash,redirect,request,abort)


from interNect import bcrypt,db
from interNect.company.forms import CompanyRegistrationForm


# import models here 
# import forms here
# from flask_login import login_user,current_user,logout_user,login_required




company=Blueprint('company',__name__)

@company.route('/register',methods=['GET','POST'] )
def register():
    form=CompanyRegistrationForm()
    if form.validate_on_submit():
        print()
        print()
        print(form.company_name.data)
        print()
        print()
    return render_template('company_register.html',form=form)

 