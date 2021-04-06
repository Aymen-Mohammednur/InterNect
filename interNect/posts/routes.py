from flask import (Blueprint, render_template,url_for,
                    flash,redirect,request,abort,jsonify)
# from flask_login import current_user,login_required,current_user
from interNect import db
# import models here 
# import forms here





posts=Blueprint('posts',__name__)

