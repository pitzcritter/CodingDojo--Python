from __future__ import unicode_literals
from .models import User
from ..review.models import Book # import Book table from apps review
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    #if type(result) == list:
    if result[0] == False:
        for err in result[1]:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result[1].id
    messages.success(request, "Registration Successful!")
    return HttpResponseRedirect(reverse("review:index"))  ### 

def login(request):
    result = User.objects.validate_login(request.POST)
    #if type(result) == list:
    if result[0] == False:
        for err in result[1]:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result[1].id
    messages.success(request, "Login successfull!")
    return HttpResponseRedirect(reverse("review:index")) ####

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

#def success(request):
#    try:
#        request.session['user_id']
#    except KeyError:
#        return redirect('/')
#    context = {
#        'user': User.objects.get(id=request.session['user_id'])
#    }
#    return render(request, 'login/success.html', context)

def show_user(request, user_id):
    user = User.objects.get(id=user_id)
    #reviews_left is reltedname...
    unique_ids = user.reviews_left.all().values("book").distinct() #####333333333333333333
    unique_books = []
    for book in unique_ids:
        unique_books.append(Book.objects.get(id=book['book']))
    context = {
        'user': user,
        'unique_book_reviews': unique_books
    }
    return render(request, 'login/user.html', context)
