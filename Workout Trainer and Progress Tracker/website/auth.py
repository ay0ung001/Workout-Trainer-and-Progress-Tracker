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
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # each user must have a unique email
    if user: 
      if check_password_hash(user.password, password): # if we find a user, check if the password is equal to the hash stored in server
        flash('logged in successfully.', category='success')
      else: 
        flash('incorrect password, try again.', category='error')
    else: 
      flash('user does not exist.', category='error')

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

    user = User.query.filter_by(email=email).first() 
    if user: 
      flash('email already exists.', category='error')
    elif len(email) < 4:
      flash('email must be greater than 3 characters.', category='error')
    elif len(first_name) < 2: 
      flash('first name must be greater than 1 character.', category='error')
    elif password1 != password2: 
      flash('passwords do not match.', category='error')
    elif len(password1) < 7: 
      flash('password must be at least 7 characters.', category='error')
    else: 
      new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
      flash('account created.', category='success')
      db.session.add(new_user)
      db.session.commit()
      return redirect(url_for('views.home'))
  return render_template("sign_up.html") 