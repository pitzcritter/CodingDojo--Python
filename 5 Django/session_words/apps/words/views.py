from django.shortcuts import render, redirect#, HttpResponse
  # the index function is called when root is visited
from time import gmtime, strftime

def index(request):
    return redirect('/words')

def words(request):
    if 'words' in request.session:
        context = {
            "words": request.session['words']
        }
        return render(request, 'words/words.html', context)
    return render(request, 'words/words.html')



def add_word(request):
    if request.method == "POST":
        print "Post"
        word  = request.POST['new_word']
        color = request.POST['color']
        when = strftime("%Y-%m-%d %H:%M %p", gmtime()) 
        if 'big' in request.POST:
            size = 'big'
        else:
            size = 'normal'
        if 'words' not in request.session:
            request.session['words'] = []

    newWord = {
        'word':  word,
        'color': color,
        'size':  size,
        'when': when
    }

    words = request.session['words']
    words.append(newWord)
    request.session['words'] = words
    for word in request.session['words']:
        print(word)
    return redirect('/words')

def return_words(request):
    return render(request, 'words/words.html')



def clear(request):
    request.session['words'] = []
    return redirect('/words')

