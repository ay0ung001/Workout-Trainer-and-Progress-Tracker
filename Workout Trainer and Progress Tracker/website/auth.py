from flask import Blueprint, redirect, render_template, request, flash, url_for 
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__) # blueprint for flask application 

@auth.route('/goals')
def goals():
  return render_template("goals.html")

@auth.route('/login', methods=['GET', 'POST']) # accepting get and post requests
def login():
  data = request.form
  print(data) # immutable multi dict
  return render_template("login.html")

@auth.route('/logout')
def logout():
  return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST']) # url = get request, submit = post rqeuest
def sign_up():
  if request.method == "POST":
    email = request.form.get('email')
    first_name = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 4:
      flash('email must be greater than 3 characters', category='error')
    elif len(first_name) < 2: 
      flash('first name must be greater than 1 character', category='error')
    elif password1 != password2: 
      flash('passwords do not match', category='error')
    elif len(password1) < 7: 
      flash('password must be at least 7 characters', category='error')
    else: 
      new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
      flash('account created.', category='success')
      db.session.add(new_user)
      db.session.commit()
      return redirect(url_for('views.home'))
  return render_template("sign_up.html") 