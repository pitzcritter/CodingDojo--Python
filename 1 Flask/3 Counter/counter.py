from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'duh' 
# our index route will handle rendering our form
@app.route('/')
def count():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/addtwo', methods=['POST'])
def incr():
  print "add 2..."
   # we'll talk about the following two lines after we learn a little more
   # about forms  
  #session['email'] = request.form['email']   # redirects back to the '/' route
  session['counter'] += 1
  return redirect('/')

@app.route('/resetcount', methods=['POST'])
def resettozero():
    session['counter'] = 0
    return redirect('/')
    #return render_template('result.html')
    #return render_template('result.html', name=session['counter'])
  #return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

app.run(debug=True) # run our server