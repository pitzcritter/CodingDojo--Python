from flask import Flask, render_template, request, redirect, flash, session
#mysql import
from mysqlconnection import MySQLConnector
#from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key = "jfdkal;"
#bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'emails')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=["POST"])
def validate():
    query = "SELECT * FROM emails WHERE address = :email"
    data = {
        'email': request.form['email'],
    }
    results = mysql.query_db(query,data) # [] , [{}]
    session['email_address'] = request.form['email']
    print "session " , session['email_address']
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    if len(request.form['email']) < 1:
        print "Email cannot be blank!"
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        print "Invalid Email Address!"
        flash("Invalid Email Address!")
        return redirect('/')
    elif len(results) > 0:
        if request.form['email'] == results[0]['address']:
            flash(request.form['email'] + " is already in system!")
            return redirect('/')    
    else:
        print "Success!"
        flash("Success!")
        query = "INSERT INTO emails (address, created_at, updatd_at) VALUES (:email, NOW(), NOW())"
        data = {'email': request.form['email']}
        email_address = mysql.query_db(query,data)        
        emails = mysql.query_db("SELECT * FROM emails")
        return render_template('success.html', all_emails=emails, validemail=request.form['email'])        

app.run(debug=True)