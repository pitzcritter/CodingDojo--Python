from flask import Flask, render_template, request, redirect#, session

app = Flask(__name__)
app.secret_key = 'duhduh' 
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ninja')
def show():
    ninjas = {
        'orange':'michelangelo',
        'blue':'leonardo',
        'red':'raphael',
        'purple':'donatello'
    }    
    files = {
        'orange':'michelangelo.jpg',
        'blue':'leonardo.jpg',
        'red':'raphael.jpg',
        'purple':'donatello.jpg'
    }    
    
    return render_template('show.html',  files=files)

@app.route('/ninja/<color>')
def show1(color):
    ninjas = {
        'orange':'michelangelo',
        'blue':'leonardo',
        'red':'raphael',
        'purple':'donatello'
    }    
    files = {
        'orange':'michelangelo.jpg',
        'blue':'leonardo.jpg',
        'red':'raphael.jpg',
        'purple':'donatello.jpg'
    }    
    #characters=[]    
    #images=[]
    #if color in ninjas:        
    #    characters.append(ninjas[color])
    #    images.append(image[color])
    #else:
    #    characters.append('notapril')
    #    images.append('notapril.jpg')
    #characters = {color: " url_for('static', filename='" + ninjas[color] + ".jpg') "}
    
    if color in ninjas:
        images = {color:files[color]}
    else:
        images = {'black':'notapril.jpg'}

    return render_template('show.html', files = images)#, character=character)

@app.route('/ninja/<color1>/<color2>')
def show2(color1, color2):
    ninjas = {
        'orange':'michelangelo.jpg',
        'blue':'leonardo.jpg',
        'red':'raphael.jpg',
        'purple':'donatello.jpg'
    }
    found = True        
    if color1 in ninjas:
        c1 = color1
        ninja1 = ninjas[color1]
        found = True
    else:
        c1 = 'black'
        ninja1 ='notapril'

    if color2 in ninjas:
        c2 = color2
        ninja2 = ninjas[color2]
        found = True
    if found:        
        images = {c1: ninja1, c2: ninja2}
    else:
        images = {'black': 'notapril'}
        #Flash(item)
    #characters = {'red':" url_for('static', filename='raphael.jpg') "}
    return render_template('show.html', files = images)#characters=characters, images=images     )#, character=character)

@app.route('/ninja/<color1>/<color2>/<color3>')
def show3(color1, color2, color3):
    print color1
    ninjas = {
        'orange':'michelangelo',
        'blue':'leonardo',
        'red':'raphael',
        'purple':'donatello'
    }
    found= False
    if color1 in ninjas:
        c1 = color1
        ninja1 = ninjas[color1]
        found = True
    else:
        c1 = 'black'
        ninja1 ='notapril'

    if color2 in ninjas:
        c2 = color2
        ninja2 = ninjas[color2]
        found = True

    if color3 in ninjas:
        c3 = color3
        ninja3 = ninjas[color3]
        found = True
    if found:
        characters = {c1: ninja1, c2: ninja2, c3: ninja3}
    else:
        characters = {'black': 'notapril'}

    characters = {color1: ninjas[color1], color2: ninjas[color2], color3: ninjas[color3]}
    #print dict['color1']
    return render_template('show.html', characters = characters)
app.run(debug=True)