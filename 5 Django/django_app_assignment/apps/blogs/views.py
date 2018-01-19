from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "Blog request!"
    return HttpResponse(response)
    # / - display "placeholder to later display all the list of blogs" via HttpResponse. 
    # Have this be handled by a method named 'index'.
def new(request):
    response = "new blog"
    print "New blog..."
    return HttpResponse(response)
# /new - display "placeholder to display a new form to create a new blog" via HttpResponse. 
# Have this be handled by a method named 'new'.
def create(request):
    response = "create"
    print "Create blog..."
    return redirect('/')
# /create - Have this be handled by a method named 'create'.  
# For now, have this url redirect to /.
def show(request, number):
    response = "blog ", number
    print "blog ", number
    return HttpResponse(response)
#/{{number}} - display 'placeholder to display blog {{number}}'.  
# For example /15 should display a message 'placeholder to display blog 15'.  
# Have this be handled by a method named 'show'.
def edit(request, number):
    response = "edit ", number
    print "edit ", number
    return HttpResponse(response)
# /{{number}}/edit - display 'placeholder to edit blog {{number}}.  
# Have this be handled by a method named 'edit'.
def destroy(request, number): # from delete
    response = "delete, destroyed " , number
    return redirect('/', response)
# /{{number}}/delete - Have this be handled by a method named 'destroy'. 
# For now, have this url redirect to /. 