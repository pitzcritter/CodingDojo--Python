from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "First Django App request!"
    print "Django Response.........."
    return HttpResponse(response)
