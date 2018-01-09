from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'duh' 
# The random module has many useful functions. This is one that gives a random number in a range
# our index route will handle rendering our form
@app.route('/')
def count():    
    session['targetnum'] = random.randrange(1, 100)
    session['result'] = ""
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    #print "add 2..."
    print "ss"
   # we'll talk about the following two lines after we learn a little more
   # about forms  
  #session['email'] = request.form['email']   # redirects back to the '/' route
    if session['targetnum'] == int(request.form['guess']):
        session['result'] = 'win!'
    elif session['targetnum'] < int(request.form['guess']):        
        session['result'] = 'too high'
    else:
        session['result'] = 'too low'
    #return redirect('/')
    return render_template("index.html", result=session['result'])

@app.route('/reset')
def reset():
    session.pop('targetnum')
    session.pop('result')
    #print "add 3..."    
    return redirect('/')

app.run(debug=True) # run our server