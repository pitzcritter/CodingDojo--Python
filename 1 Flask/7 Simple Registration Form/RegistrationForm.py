from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)#, template_folder='templates')
app.secret_key="urgh"
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[0-9])')

# See week2 code review 
@app.route('/')
def index():
    #if 'data' in session.keys():
    #    email = session['data']['email']
    #    password = session['data']['password']
    #    confirmpassword = session['data']['confirmpassword']
    #    firstname = session['data']['firstname']
    #    lastname = session['data']['lasstname']
        #flash('name: ' + name)
        #flash('location: ' + location)
        #flash('language: ' + language)
        #flash('comment: ' + comment)
    #    return render_template('index.html')#, name=name, location=location, language=language, comment=comment)
    #else:
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    email = request.form['email']
    password = request.form['password']
    confirmpassword = request.form['confirmpassword']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    approve = True    

    session['data'] = {
        'email': email,
        'password': password,
        'confirmpassword': confirmpassword,
        'firstname': firstname,
        'lastname': lastname
    }
    
    #flash(session['data']['language'])
    #flash(session['data']['location'])
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        approve = False
    else:
        flash("Email success!")
        print "Email success!"        

    if firstname == '':
        flash('first name is empty')
        print 'first name is empty'
        approve = False
    elif not firstname.isalpha():
        flash('first name is must be alphanumeric')
        print 'first name is must be alphanumeric'
        approve = False
    if lastname == '':
        flash('last name is empty')
        print 'last name is empty'
        approve = False
    elif not lastname.isalpha():
        flash('last name is must be alphanumeric')
        print 'last name is must be alphanumeric'
        approve = False
    if len(password) > 8:    
        flash('password must be less than 8 characters')
        print 'password must be less than 8 characters'
        approve = False
    if not confirmpassword == password:    
        flash('passwords do not match')
        print 'passwords do not match'
        approve = False
    if approve:                
        return render_template('result.html')#, name=name, location=location, language=language, comment=comment)
    else:
        print 'returning'
        return redirect('/')

@app.route('/returnindex', methods=["POST"])
def returnindex():
    print 'returning to index.html'
    return redirect('/')    

app.run(debug=True)

# Assignment: Dojo Survey With Validation
# Take the Dojo Survey assignment that you completed previously and add validations! 
# The Name and Comment fields should be validated so that they are not blank. 
# Also, validate that the comment field is no longer than 120 characters.
