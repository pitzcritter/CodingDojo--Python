from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.  
  # the index function is called when root is visited
  #def index(request):
  #  response = "Hello, I am your first request!"
  #  return HttpResponse(response)


#from django.http import HttpResponse, Http404, HttpResponseNotFound
#from django.shortcuts import render
#from datetime import datetime

def index(request):
    #date = datetime.now().date().strftime('%B %-d, %Y')
    #time = datetime.now().time().strftime('%-I:%M %p')
    date = strftime("%Y-%m-%d", gmtime())
    time = strftime("%H:%M %p", gmtime())
    context = {
        'datetime' : [
            {'date': date},
            {'time': time},
        ]
    }
    return render(request, 'date_time/index.html', context) # updated this line