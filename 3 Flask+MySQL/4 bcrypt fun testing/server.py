from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt()
app.secret_key='this'
mysql = MySQLConnector(app,'bcryptdb')
import re

def validate():
    valid = True
    #Check first name
    if len(request.form['first_name']) > 1:
        print 'First name must be at least 2 characters!'
        flash('First name must be at least 2 characters!')
        valid = False    
    if any(char.isdigit() for char in request.form['first_name']) == True:
        print 'First name cannot have numbers'
        flash('First name cannot have numbers')
        valid = False

    #Check last name
    if len(request.form['last_name']) > 1:
        print 'Last name must be at least 2 characters!'
        flash('Last name must be at least 2 characters!')
        valid = False
    if any(char.isdigit() for char in request.form['last_name']) == True:
        print 'Last name cannot have numbers'
        flash('Last name cannot have numbers')
        valid = False

    #Check email
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    if request.form['email'] == '':
        print "Email cannot be blank!"
        flash("Email cannot be blank!")
        valid = False
    #    pass
    elif not EMAIL_REGEX.match(request.form['email']):
        print "Invalid Email Address!"
        flash("Invalid Email Address!")
        valid = False
    #    pass
    #else:
    #    pass

    if request.form['password'] == '':
        print "Password cannot be blank!"
        flash("Password cannot be blank!")
        valid = False
    elif len(request.form['password']) < 8:
        print "Password must be atleast 8 characters!"
        flash("Password must be atleast 8 characters")
        valid = False
    
    if request.form['password'] != request.form['confirm_password']:
        print "Password does not match confirmation!"
        flash("Password does not match confirmation!")
        valid = False

    query_data = { 'email': request.form['email'] }
    exist_email = mysql.query_db("SELECT * FROM users WHERE email = :email LIMIT 1", query_data) # user will be returned in a list
    if len(exist_email) > 0:
        print "Email already in use!"
        flash("Email already in use!")
        valid = False

    #See if there are any errors
    if valid:
        session['login']=True
        return True
    else:
        session['login']=False
        return False
        
def validate_pw(dbaseData):
    print "in val pw"
    print "em: " , dbaseData[0]['email']
    if session['email'] != dbaseData[0]['email']:
        print "email does not match for user!"
        flash("email does not match for user!")
        return False
    data = { 'email': dbaseData[0]['email'] }    
    #user = mysql.query_db("SELECT * FROM users WHERE email = :email LIMIT 1", data) # user will be returned in a list        
    #print "user: ", user
    #password = mysql.query_db("Select password From users Where id = '{}'".format(id),data)
    #print "validate pw: ", request.form['password'] , "  " , password
    if bcrypt.check_password_hash(dbaseData[0]['password'], bcrypt.generate_password_hash(session['password'])):
        print "validated pw"
        return True
    else:
        print "Password does not match! Action failed!"
        flash("Password does not match! Action failed!")
        return False    
    
@app.route('/')
def index():
    session.clear()
    session['login']=False
    print type(mysql)
    users = mysql.query_db("SELECT * FROM users")
    print users
    return render_template('index.html',all_users=users)

# get form data and insert it into database
@app.route('/users', methods=['POST'])
def create():    
    if validate():    
        session['first_name']=request.form['first_name']
        session['last_name']=request.form['last_name']
        session['email']=request.form['email']
        session['password']=request.form['password']
        session['confirm_password']=request.form['confirm_password']        
        session['login']=True
        # we want to insert into out query
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name,last_name,email,password,created_at,updated_at)values(:first_name,:last_name,:email,:pw_hash,NOW(),NOW())"
        # we will then create a dictionary of data from the POST data received.
        data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':request.form['password']}
        # Run query    
        mysql.query_db(query,data)
        query = mysql.query_db("Select id From users Where first_name=:first_name And last_name=:last_name",data)
        session['id']=query[0]['id']
        print "query:  ", query
        print "id: ",session['id']
        #print session['id'][0]['id']
    else:
        session['login']=False
    return redirect('/')

# <id> here is like a placeholder, it doesn't need to match with the one in HTML
@app.route('/users/<id>/edit',methods=['GET'])
def edit(id):
    print 'In edit. id= ',id
    query = "SELECT * FROM users WHERE id = :specific_id"
    data = {'specific_id':id}
    user = mysql.query_db(query,data)
    print 'in edit, user= ', user
    first_name = user[0]['first_name']  # retrieve value for each key
    last_name = user[0]['last_name']
    email = user[0]['email']
    password = user[0]['password']
    print password
    return render_template('edit.html', first_name=first_name, last_name=last_name,email=email,password=password,id=id)

@app.route('/users/<id>/delete', methods=['POST'])
def delete(id):
    print 'In delete, id = ', id
    print "EM: ", request.form['email']
    print "PW: ", request.form['password']
    #print 'delete password: ', mysql.query_db("Select password From users Where id = '{}'".format(id),data)
    #password = mysql.query_db("Select password From users Where id = '{}'".format(id),data)
    data = {'specific_id':id}
    dbaseData = mysql.query_db("Select * From users Where id = :specific_id", data)
    if validate_pw(dbaseData):
        # write query to delete based on id
        print "validated pw, now delete"
        query = "DELETE FROM users WHERE id = :specific_id"

        data = {'specific_id':id}
        mysql.query_db(query, data)                    
    return redirect('/')

# Update Existing Records
@app.route('/users/<id>',methods=['POST'])
def update(id):
    print 'begin update, id= ',id
    query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, password = :password WHERE id = :id"
    print "query " + query
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'id':id
    }
    print "updating !!!!!!!!!!!!!"
    mysql.query_db(query,data)
    return redirect('/')

app.run(debug=True)