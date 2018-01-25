from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


# /users - display 'placeholder to later display all the list of users'
def index(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

# /register - display 'placeholder for users to create a new user record'
# /users/new - have the same method that handles /register also handle the url request of /users/new
def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

# /login - display 'placeholder for users to login' 
def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)