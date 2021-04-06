from flask import (Blueprint, render_template,url_for,
                    flash,redirect,request,abort)


from interNect import bcrypt,db


# import models here
# import forms here
# from flask_login import login_user,current_user,logout_user,login_required




intern=Blueprint('intern',__name__)



 