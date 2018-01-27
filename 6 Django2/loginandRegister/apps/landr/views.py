from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
# Create your views here.

def index(request):
    print "landr/index.html:::::"    
    return render(request, "landr/index.html")

def login(request):
    print "request.POST: ",request.POST
    errors = User.objects.login_validate(request.POST)
    print 'errors:', errors
    print 'type(errors): ',type(errors)
    print type(errors) == list
    if type(errors) == list:
        #for tag, err in errors.iteritems():
        #    messages.error(request, err, extra_tags=tag)
        #    return redirect('/blog/edit/'+id)
        if len(errors) > 0:
            for err in errors:
                messages.error(request, err)
            return redirect('/') 
    print "email: ",request.POST['email']           
    request.session['user_id'] =errors.id
    #request.session['user_id'] = request.POST['email']
    messages.success(request, "Successfully logged in!")
    return redirect("/success",request)

def register(request):
    print "request"
    errors = User.objects.registration_validate(request.POST)
    print "errors: ", errors
    if type(errors) == list:
        for err in errors:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = errors.id
    messages.success(request, "Successfully registered!")
    print "req1::::"
    return redirect("/success",request)

def success(request):
    print "success@@@@@@@@@@@@@@@@@@@@@@@@@@"
    try:
        request.session['user_id']
        print "request.session['user_id']: ", request.session['user_id']
    except KeyError:
        print "excxept:::::::"
        return redirect('/')
    print "User.objects.get(id=request.session['user_id']): ", User.objects.get(id=request.session['user_id'])
    return render(request, "landr/success.html",{'user': User.objects.get(id=request.session['user_id'])})
