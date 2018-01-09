from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)#, template_folder='templates')
#app.secret_key="urgh"
#week2 code review 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']     
    return render_template('result.html', name=name, location=location, language=language, comment=comment)
    #return render_template('result.html', name=name, location=location, language=language, comment=comment)
    # redirects back to the '/' route
    #return redirect('/')
app.run(debug=True)