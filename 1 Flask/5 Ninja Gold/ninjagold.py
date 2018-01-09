from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'duhduh' 
comment = []

# The random module has many useful functions. This is one that gives a random number in a range
# our index route will handle rendering our form
@app.route('/')
def base():    
    session['gold'] = 0
    session['farmgold'] = 0
    session['thisstr'] = ''
    return render_template("index.html", gold=session['gold'])
    #return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    timestr = datetime.datetime.now().strftime("%Y/%m/%d %H:%M %p")
    if request.form['building'] == 'farm':
        session['farmgold'] = random.randrange(10, 21)
        session['gold'] += session['farmgold']
        comment.append("Earned " + str(session['farmgold']) + " golds from the farm! (" + timestr + ")")
        session['thisstr'] = session['comment'] + "\nEarned " + str(session['farmgold']) + " golds from the farm! (" + timestr + ")"
    
    if request.form['building'] == 'cave':
        session['cavegold'] = random.randrange(5, 11)
        session['gold'] += session['cavegold']
        comment.append("Earned "+ str(session['cavegold']) + " golds from the cave! (" + timestr + ")")
        session['thisstr'] = session['comment'] + "\nEarned "+ str(session['cavegold']) + " golds from the cave! (" + timestr + ")"
    
    if request.form['building'] == 'house':
        session['housegold'] = random.randrange(2, 6)
        session['gold'] += session['housegold']
        comment.append("Earned "+ str(session['housegold']) + " golds from the house! (" + timestr + ")")
        session['thisstr'] = session['comment'] + "\nEarned "+ str(session['housegold']) + " golds from the house! (" + timestr + ")"

    if request.form['building'] == 'casino':
        session['casinogold'] = random.randrange(0, 51)                
        if  random.randrange(1, 3) == 1:
            session['gold'] -= session['casinogold']
            comment.append("Entered a casino and lost " + str(session['casinogold']) + " golds!  Ouch! (" + timestr + ")")
            session['thisstr'] = session['comment'] + "\nEntered a casino and lost " + str(session['casinogold']) + " golds!  Ouch! (" + timestr + ")"
        else:
            session['gold'] += session['casinogold']
            comment.append("Entered a casino and earned " + str(session['casinogold']) + " golds! (" + timestr + ")")
            session['thisstr'] = session['comment'] + "\nEntered a casino and earned " + str(session['casinogold']) + " golds! (" + timestr + ")"
    session['comment'] = session['thisstr']
    return render_template("index.html", gold=session['gold'])
    #return redirect('/')

app.run(debug=True) # run our server