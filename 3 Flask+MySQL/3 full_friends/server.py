from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriends')
app.secret_key = 'ohwell'
import re
def validate():
    valid = True
    #Check first name
    if request.form['first_name'] == '':
        flash('First name cannot be blank')
        valid = False
        pass
    elif any(char.isdigit() for char in request.form['first_name']) == True:
        flash('First name cannot have numbers')
        valid = False
        pass
    else:
        pass

    #Check last name
    if request.form['last_name'] == '':
        flash('Last name cannot be blank')
        valid = False
        pass
    elif any(char.isdigit() for char in request.form['last_name']) == True:
        flash('Last name cannot have numbers')
        valid = False
        pass
    else:
        pass

    #Check email
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    if request.form['email'] == '':
        print "Email cannot be blank!"
        flash("Email cannot be blank!")
        pass
    elif not EMAIL_REGEX.match(request.form['email']):
        print "Invalid Email Address!"
        flash("Invalid Email Address!")
        pass
    else:
        pass


    #See if there are any errors
    if valid:
        return True
    else:
        return False


@app.route('/')
def index():    
    results = mysql.query_db("SELECT * FROM fullfriends")
    print "results 1"
    print results
    return render_template('index.html', list=results)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO fullfriends (firstname, lastname, email, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['email'])
    print "query 1"
    print query
    if validate():
        print "send to dbase!!!!!!!!!!!!!!!!!!!!!!!!!"
        results = mysql.query_db(query)
        print "Insert:"
        print results
        id = mysql.query_db("Select 'Id' From fullfriends Where firstname = '{}' And lastname = '{}'".format(request.form['first_name'], request.form['last_name']))
        print "IIIIIIIIIIIIDDDDDDDD"
        print id
    return redirect('/')

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    print "Update dbase!!!!!!!!!!!!!!!!!!!!!!!!!"
    print id
    query = "UPDATE fullfriends SET firstname = '{}', lastname = '{}', email = '{}', updated_at = NOW() WHERE Id = {}".format(request.form['first_name'], request.form['last_name'], request.form['email'], int(id))
    print "query 2"
    print query
    if validate():
        #mysql.run_mysql_query(query)
        results = mysql.query_db(query)
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM fullfriends WHERE Id = '{}'".format(id)
    print "query 3"
    print query
    #friendData = mysql.fetch(query)
    results = mysql.query_db(query)
    print results
    return render_template('edit.html', friend=results)

@app.route('/friends/<id>/delete', methods=['POST'])
#def printthis():
#    print 'this'
def destroy(id):
    print "delete:"
    print id
    query = "DELETE FROM fullfriends WHERE Id = '{}'".format(id)
    print "query 4"
    print query
    #mysql.run_mysql_query(query)
    results = mysql.query_db(query)
    return redirect('/')

app.run(debug=True)