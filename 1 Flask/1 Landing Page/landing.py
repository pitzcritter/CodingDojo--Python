from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninjas')
def ninja_page():
	return render_template('ninjas.html')

@app.route('/dojos/new')
def new_dojo():
	return render_template('dojos.html')

app.run(debug=True)