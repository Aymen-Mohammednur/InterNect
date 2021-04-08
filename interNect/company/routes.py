from flask import (Blueprint, render_template,url_for,
                    flash,redirect,request,abort)


from interNect import bcrypt,db
from interNect.company.forms import CompanyRegistrationForm
from interNect.models import Company


# import models here 
# import forms here
# from flask_login import login_user,current_user,logout_user,login_required




company = Blueprint('company',__name__)

@company.route('/register',methods=['GET','POST'] )
def register():
    form = CompanyRegistrationForm()
    if form.validate_on_submit():
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        company = Company(company_name=form.company_name.data, email=form.email.data, 
                        password=encrypted_password, street_address=form.street_address.data, 
                        phone_number=form.phone_number.data, category=form.category.data, 
                        description=form.description.data, postal_code=form.postal_code.data)
        
        db.session.add(company)
        db.session.commit()

        flash(f'Company account has been created.')
        return redirect(url_for('main.login'))

    return render_template('company_register.html',form=form)

 