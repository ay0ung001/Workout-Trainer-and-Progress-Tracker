from flask import Blueprint, render_template, request, flash 

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
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 4:
      flash('email must be greater than 3 characters', category='error')
    elif len(firstName) < 2: 
      flash('first name must be greater than 1 character', category='error')
    elif password1 != password2: 
      flash('passwords do not match', category='error')
    elif len(password1) < 7: 
      flash('password must be at least 7 characters', category='error')
    else: 
      flash('account created.', category='success')
  return render_template("sign_up.html") 