from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from random import randrange, random, choice

# the index function is called when root is visited
def index(request):
    #response = "Hello, I am your first request!"
    #rand_num = request.session.get('rand_num', randrange(1,10))
    #print "request.session.get('rand_num'): ", request.session.get('rand_num')
    if not 'rand_num' in request.session:
        request.session['rand_num'] = randrange(1,10)
    #    print "wow: ", request.session['rand_num']
    #if not request.session['rand_num']:
    #request.session['rand_num'] = randrange(1,10)
    #rand_num = "ek"
    #context = {
    #  "rand": strftime("%Y-%m-%d %H:%M %p", gmtime())      
    #}

    #return HttpResponse(response)
    return render(request,'generate_word\index.html')

def random_word(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    word = ''
    these_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    first_index = randrange(0,11)
    #for num in range (first_index, first_index + randrange(5,15)):
    for num in range (1, randrange(4,14)):# will include spaces as potential characters so that word length can be shorrt.
        word = word + choice(these_letters)
    print 'word: ', word
    words = {
        'random_word': word
    }
    return render(request, 'generate_word/index.html', words)

def reset(request):
    request.session.clear()
    return redirect('/')    
