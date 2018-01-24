from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# the index function is called when root is visited
def index(request):
    #response = "Hello, I am your first request!"
    return render(request, 'survey\index.html')

def process_input(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    if request.method == "POST":
        print "Post"
        print request.POST
        print "Name: ", request.POST['name']
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']   
        request.session['when'] = strftime("%Y-%m-%d %H:%M %p", gmtime()) 

    #return render(request, 'survey\results.html')
        #return redirect('f/result')
        return redirect('/results')
    else:
        print "Not Post"
        return redirect('/')

def view_results(request):    
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment']
    }
    print "results.html"
    return render(request, 'survey\\results.html', context)    

def go_back(request):
    print "Go Back"
    return redirect('/')