from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'aksdf'
mysql = MySQLConnector(app,'loginandregister')
bcrypt = Bcrypt(app)

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

def validate():
    validate = True
    #Check first name
    if len(request.form['first_name']) < 1:
        flash('First name must be at least 2 characters!','firstNameError')
        validate = False
    elif any(char.isdigit() for char in request.form['first_name']) == True:
        flash('First name cannot have numbers','firstNameError')
        validate = False
    else:
        session['first_name'] = request.form['first_name']

    #Check last name
    if len(request.form['last_name']) < 1:
        flash('Last name must be at least 2 charactoers!','lastNameError')
        validate = False        
    elif any(char.isdigit() for char in request.form['last_name']) == True:
        flash('Last name cannot have numbers','lastNameError')
        validate = False
    else:
        session['last_name'] = request.form['last_name']

    #Check email
    if request.form['email'] == '':
        flash('Email cannot be blank','emailError')
        validate = False
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address','emailError')
        validate = False        
    else:
        session['email'] = request.form['email']

    #Check password
    if request.form['password'] == '':
        flash('Password cannot be blank', 'passwordError')
        validate = False
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters', 'passwordError')
        validate = False
    elif not passwordRegex.match(request.form['password']):
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'passwordError')
        validate = False
    else:
        session['password'] = request.form['password']

    #Check confirmation password
    if request.form['confirm_password'] == '':
        flash('Please confirm password', 'confirm_passwordError')
        validate = False
    elif request.form['confirm_password'] != request.form['password']:
        flash('Passwords do not match', 'confirm_passwordError')
        validate = False
    else:
        session['confirm_password'] = request.form['confirm_password']

    #See if there are any errors
    if validate:
        return True
    else:
        session['password'] = ''
        session['confirm_password'] = ''
        return False

def validateLogin():
    errors = 0
     #Check email
    if request.form['email'] == '':
        flash('Email cannot be blank', 'emailError')
        validate = False
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'emailError')
        validate = False
    else:
        session['email'] = request.form['email']

    #Check password
    if request.form['password'] == '':
        flash('Password cannot be blank', 'passwordError')
        validate = False
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters', 'passwordError')
        validate = False
    elif not passwordRegex.match(request.form['password']):
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'passwordError')
        validate = False
    else:
        session['password'] = request.form['password']

        #See if there are any errors
    if validate:
        return True
    else:
        session['password'] = ''
        session['confirm_password'] = ''
        return False

@app.route('/')
def index():
    #orderId = request.session.get('orderId',ts)
    if session.get('first_name'):
        session['first_name'] = ''
    if session.get('last_name'):
        session['last_name'] = ''
    if session.get('email'):
        session['email'] = ''
    if session.get('password'):
        session['password'] = ''
    if session.get('confirm_password'):
        session['confirm_password'] = ''
    if session.get('user_id'):
        session['userid'] = ''

    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if validate() == False:
        return redirect('/')
    else:
        encrypted_password = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :encrypted_password, NOW(), NOW())"
        data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'encrypted_password':encrypted_password}
        mysql.query_db(query,data)        
        session['password'] = ''
        session['confirm_password'] = ''
    return redirect('/dashboard')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validate', methods=['POST'])
def validateLoginInfo():
    if validateLogin() == False:
        return redirect('/login')
    else:
        userInfo = mysql.query_db("SELECT * FROM users WHERE email = '{}'".format(session['email']))
        inputPassword = request.form['password']
        inputPasswordEncrypted = bcrypt.generate_password_hash(request.form['password'])

        if inputPasswordEncrypted == userInfo[0]['password']:
            return redirect('/dashboard')
        else:
            flash('Incorrect password', 'passwordError')
    return redirect('/login')

@app.route('/dashboard')
def returnDashboard():
    if session['email']:
        return render_template('dashboard.html')
    else:
        return redirect('/')

@app.route('/logout', methods=['POST'])
def clear():
    #session['first_name'] = ''
    session['last_name'] = ''
    session['email'] = ''
    session['password'] = ''
    session['confirm_password'] = ''
    session['userid'] = ''

    return redirect('/')

app.run(debug=True)

#Assignment: Login and Registration
#We've learned about how we can connect to the database, insert records posted from a form, retrieve records from a database and set a session/flash for any error or success messages that we get along the way. One of the major components to every website is a login and registration.
#Registration
#The user inputs their information, we verify that the information is correct, insert it into the database and return back with a success message. If the information is not valid, redirect to the registration page and show the following requirements:
#Validations and Fields to Include
#1.	First Name - letters only, at least 2 characters and that it was submitted
#2.	Last Name - letters only, at least 2 characters and that it was submitted
#3.	Email - Valid Email format, and that it was submitted
#4.	Password - at least 8 characters, and that it was submitted
#5.	Password Confirmation - matches password
#Login
#When the user initially registers we would log them in automatically, but the process of "logging in" is simply just verifying that the email and password the user is providing matches up with one of the records that we have in our database table for users.
#But how do we keep track of them once they've logged in? I think you might already know... It's using session! We can create a session variable that holds the user's id. From our study in Database Design, we know that if we have the id of any table we can gather the rest of the information that is associated with that id. Storing a single session variable with the user's id is all we need to access all the information associated with that user.
#Once we have already identified the places on our site that we wish to be dynamic for users that are logged in, then we just need to check to see if that session variable has been set and display the content accordingly.
