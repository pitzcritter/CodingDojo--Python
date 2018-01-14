from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import datetime
import re

from itertools import groupby
import pprint

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wall')
app.secret_key = 'SHHHHH!'

passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

def validate():
    valid=True
    #Check first name
    if request.form['first_name'] == '':
        flash('Name cannot be blank', 'first_nameError')
        valid=False
    elif any(char.isdigit() for char in request.form['first_name']) == True:
        flash('Name cannot have numbers', 'first_nameError')
        valid=False
    else:
        session['first_name'] = str(request.form['first_name'])

    #Check last name
    if request.form['last_name'] == '':
        flash('Name cannot be blank', 'last_nameError')
        valid=False
    elif any(char.isdigit() for char in request.form['last_name']) == True:
        flash('Name cannot have numbers', 'last_nameError')
        valid=False
    else:
        session['last_name'] = str(request.form['last_name'])

    #Check email
    if str(request.form['email']) == '':
        flash('Email cannot be blank', 'emailError')
        valid=False
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'emailError')
        valid=False
    else:
        session['email'] = str(request.form['email'])

    #Check password
    if str(request.form['password']) == '':
        flash('Password cannot be blank', 'passwordError')
        valid=False
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters', 'passwordError')
        valid=False
    elif not passwordRegex.match(request.form['password']):
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'passwordError')
        valid=False
    else:
        session['password'] = str(request.form['password'])

    #Check confirmation password
    if str(request.form['confirm_password']) == '':
        flash('Please confirm password', 'confirm_passwordError')
        valid=False
        #pass
    elif str(request.form['confirm_password']) != str(request.form['password']):
        flash('Passwords do not match', 'confirm_passwordError')
        valid=False
    else:
        session['confirm_password'] = str(request.form['confirm_password'])

    #See if there are any errors
    if not valid:
        session['password'] = ''
        session['confirm_password'] = ''

    return valid

def validateLogin():
    errors = 0
     #Check email
    valid = True
    if str(request.form['email']) == '':
        flash('Email cannot be blank', 'loginEmailError')
        valid=False
        pass
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'loginEmailError')
        valid=False
        pass
    else:
        session['email'] = str(request.form['email'])

    #Check password
    if request.form['password'] == '':
        flash('Password cannot be blank', 'loginPasswordError')
        valid=False
        pass
    else:
        session['password'] = str(request.form['password'])

        #See if there are any errors
    if not valid:
        session['password'] = ''
    
    return valid

def setUserId():
    queryUser_id = "SELECT id FROM users WHERE email = :email"
    data={"email":session['email']}
    id = mysql.query_db(queryUser_id, data)
    session['userid'] = id[0]['id']
    return True

def EmailExists():
    getEmails = "SELECT email FROM users WHERE email = :email Limit 1"    
    data = {'email':request.form['email']}
    emailList = mysql.query_db(getEmails,data)
    return len(emailList) > 0

def getMessagesWithUsers():
    getMessages = "SELECT messages.id, messages.message, messages.created_at, users.id, users.first_name, users.last_name FROM messages LEFT JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(getMessages)
    return messages

def getComments():
    getComments = "SELECT comments.message_id, comments.comment, comments.created_at, users.first_name, users.last_name FROM comments LEFT JOIN messages ON comments.message_id = messages.id LEFT JOIN users ON comments.user_id = users.id"
    comments = mysql.query_db(getComments)
    return comments

def getMessagesWithComments():
    all_comments = getComments()
    messages = getMessagesWithUsers()
    commentList = {}
    messagesWithCommentContainer = []

    for comment in all_comments:
        info = {
                "comment_id": comment["id"],#not needed
                "message_id": comment['message_id'],
                "user_id": comment['user_id'],#not needed
                "first_name": comment['first_name'],
                "last_name": comment['last_name'],
                "comment": comment['comment'],
                "created_at": comment['created_at'].strftime("%B %d, %Y %H:%M %p")
            }
        if comment['message_id'] in commentList:
            commentList[comment['message_id']].append(info)
        else:
            commentList[comment['message_id']] = [info]
    for message in messages:
        messageData = {
            "created_at": message['created_at'].strftime("%B %d, %Y %H:%M %p"),
            "message_id": message['id'],
            "first_name": message['first_name'],
            "last_name": message['last_name'],
            "message": message['message'],
            "new_id": message['created_at'].strftime("%B%d%Y-%H%M%S")
        }

        if message['id'] in commentList:
            messageData['comment'] = commentList[message['id']]
        messagesWithCommentContainer.append(messageData)
    return messagesWithCommentContainer

@app.route('/')
def index():
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
    if session.get('loggedin'):
        session['loggedin'] = False
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create(methods=["GET","POST"]):
    if validate():
        if not EmailExists():
            encryptedPassword = bcrypt.generate_password_hash(request.form['password'])
            query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email,:encryptedPassword, NOW(), NOW())"
            data={
                "first_name":session['first_name'],
                "last_name":session['last_name'], 
                "email":session['email'], 
                "encryptedPassword":encryptedPassword
            }
            mysql.query_db(query, data)
            session['password'] = ''
            session['confirm_password'] = ''
            session['loggedin'] = True
            return redirect('/dashboard')
        else:
            flash('Account with email already exists. Please use another email', 'emailError')
    else:
        session['loggedin'] = False
    return redirect('/')

@app.route('/validate', methods=['POST'])
def validateLoginInfo():
    if validateLogin():
        data = {'email':request.form['email']}
        userInfo = mysql.query_db("SELECT * FROM users WHERE email =:email", data)
        if userInfo:
            inputPassword = request.form['password']
            if bcrypt.check_password_hash(userInfo[0]['password'], inputPassword):
                session['loggedin'] = True
                session['email'] = userInfo[0]['email']
                session['userid'] = userInfo[0]['id']
                session['first_name'] = userInfo[0]['first_name']
                return redirect('/dashboard')
            else:
                flash('Incorrect password', 'loginPasswordError')
        else:            
            flash('No user with that email exists. Please create new user', 'loginEmailError')
            return redirect('/')
    else:
        session['loggedin'] = False
        return redirect('/login')
    return redirect('/dashboard')
@app.route('/dashboard')
def returnDashboard():
    if session['loggedin']:
        setUserId()
        query = "Select concat(users.id,'-', messages.id) As message_key, email, group_concat(' ' ,message, ' - ') AS messages, concat(first_name, ' ', last_name, ' - ',  date_format(messages.created_at,'%M %e, %Y')) As label, date_format(messages.created_at,'%B%d%Y-%H%M%S') As new_id From users Join messages On users.id = messages.user_id Group By users.id, concat(day(messages.created_at), month(messages.created_at), year(messages.created_at)) Order By users.id Desc, messages.id, messages.created_at;"
        message_data = mysql.query_db(query)
        messages= []
        query = "Select concat(users.id,'-', messages.id) As message_key, group_concat(' ' ,comment,' - ') As comments, concat(first_name, ' ', last_name, ' - ',  date_format(comments.created_at,'%M %e, %Y')) As label From messages Join comments On message_id = comments.message_id Join users on comments.user_id = users.id Group By comments.user_id, comments.user_id, concat(day(messages.created_at), month(messages.created_at), year(messages.created_at)) Order By comments.user_id Desc, messages.id, comments.id;"
        comment_data = mysql.query_db(query)
        comments=[]
        return render_template('dashboard.html', messagesDB=message_data, commentsDb=comment_data)
    else:
        return redirect('/')

@app.route('/message', methods=['POST'])
def messageData():
    if session['loggedin']:
        query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :postMessage, NOW(), NOW())"
        data = {
            "postMessage":request.form['message'],
            "user_id":session['userid']}
        mysql.query_db(query, data)
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/message/<message_id>/comment', methods=['POST'])
def postComment(message_id):
    if session['loggedin'] == True:
        comment = str(request.form['comment'])
        query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:messag_id, :user_id, comment, NOW(), NOW())"
        data={
            'message_id':message_id,
            "user_id":session['userid'],
            "comment":comment}
        mysql.query_db(query, data)
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/logout')
def clear():
    print "logout"
    session['first_name'] = ''
    session['last_name'] = ''
    session['email'] = ''
    session['password'] = ''
    session['confirm_password'] = ''
    session['userid'] = ''
    session['loggedin'] = False

    return redirect('/')

app.run(debug=True)