from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)#, template_folder='templates')
app.secret_key="urgh"
# See week2 code review 
@app.route('/')
def index():
    if 'data' in session.keys():
        name = session['data']['name']
        location = session['data']['location']
        language = session['data']['language']
        comment = session['data']['comment']
        flash('name: ' + name)
        flash('location: ' + location)
        flash('language: ' + language)
        flash('comment: ' + comment)
        return render_template('index.html')#, name=name, location=location, language=language, comment=comment)
    else:
        return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    approve = True    

    session['data'] = {
        'name': name,
        'location': location,
        'language': language,
        'comment': comment
    }
    
    #flash(session['data']['language'])
    #flash(session['data']['location'])
    
    if name == '':
        flash('name is empty')
        print 'name is empty'
        approve = False
    if comment == '':
        flash('commment empty')
        print 'commment empty'
        approve = False
    elif len(comment) > 10:
        flash('comment too long')
        print 'comment too long'
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
