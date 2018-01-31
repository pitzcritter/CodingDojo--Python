from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import  strftime, strptime
from .models import User, Message, Comment
from ago import human, delta2dict #https://pypi.python.org/pypi/ago     pip install ago
from django.utils import timezone # https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/
from datetime import datetime, timedelta
#from pytz import timezone

# the index function is called when root is visited
def index(request):    
    if not 'login' in request.session:
        request.session['login']=False
    return render(request,'userd\index.html')

def signin(request):
    return render(request,'userd\login.html')

def login(request):# validate login, send to dbase
    print "request.POST: ",request.POST
    result = User.objects.login_validate(request.POST)
    print 'result:', result
    print type(result) == list
    if type(result) == list:
        if len(result) > 0:
            for err in result:
                messages.error(request, err)
            request.session['login'] = False
            return redirect('/signin') 
    request.session['user_id'] =result.id
    request.session['first_name'] = result.first_name
    
    messages.success(request, "Successfully logged in!")    
    request.session['login'] = True
    return redirect("success",user_id= result.id)

def register(request):############################333
    print "new member"
    return render(request,'userd\login2.html')


def create(request):# validate registration, send to dbaase
    result = User.objects.registration_validate(request.POST)
    print "result: ", result
    print "type(result): ", type(result)
    if type(result) == list: # a list identifies that there are errors, else it is a dbase record.
        for err in result:
            messages.error(request, err)
        request.session['login'] = False
        return redirect('/')  #################################################### testing to see if redirect to login....
        return render(request,'userd\login2.html') # redirect back.....
    request.session['user_id'] = result.id
    request.session['first_name'] = result.first_name
    messages.success(request, "Successfully registered!")    
    request.session['login'] = True
    return redirect("/success/{}".format(result.id),request, {"user_id": result.id})#,result) # returns record of who is logged in...

def success(request, user_id):        
    thisList = []
    if User.objects.get(id=request.session['user_id']).user_level.usertext == 'Admin':# and request.session['user_id'] == user_id:
        for this in User.objects.all():
            thisObject= {"id": this.id, 'first_name': this.first_name, "last_name": this.last_name, 'email':this.email, 'created_at':this.created_at.strftime("%b %d, %Y"), 'user_level':this.user_level.usertext}
            thisList.append(thisObject)
#    print "request.session['user_id']: ", request.session['user_id']
        #return render(request,"admin_dashboard",{'Users':thisList})
        return render(request,"userd/admindbd.html",{'Users':thisList})
    else:        
        #for this in User.objects.exclude(user_level=2):
        for this in User.objects.all():
            thisObject= {"id": this.id, 'first_name': this.first_name, "last_name": this.last_name, 'email':this.email, 'created_at':this.created_at.strftime("%b %d, %Y"), 'user_level':this.user_level.usertext}
            thisList.append(thisObject)
        #return render(request,'user_dashboard',{'Users':thisList})
        return render(request,'userd/userdbd.html',{'Users':thisList},{'user_id':user_id})

def logoff(request):
    request.session['login'] = False
    return redirect("/")


#def dashboard(request):
#    if User.objects.isAdmin(request):
#        render(request,'userd\\admindbd.html')
#    else:
#        render(request,'userd\\userdbd.html')

def profile(request):#######################################
    return redirect('/')



def edit(request, user_id):
    print "starting user edit.html"
    record=User.objects.get(id=user_id)
    return render(request, 'userd/edit.html', {'User': User.objects.get(id=user_id), "bday": str(record.birth_date)})

def edit_update(request, user_id):
    print "edit_update"
    result = User.objects.edit_validate(request.POST, user_id)
    if result:
        print "edit data updated: ", result
        return redirect(("/users/{}/edit").format(user_id))
    else:
        messages.error(request,result)
        print "edit error result: ", result
        return redirect(("/users/{}/edit").format(user_id))

def description_update(request, user_id):
    print "description update"
    try:
        record = User.objects.get(id=user_id)
    except:
        messages.error(request,'cannot find databases record')        
        return redirect(("/users/{}/edit").format(user_id))    
    try:
        print "desc: ",request.POST['description']
        record.description =  request.POST['description']
        record.save()
    except:
        messages.error(request,'cannot update description')
        return redirect(("/users/{}/edit").format(user_id))
    print "description updated"
    return redirect(("/users/{}/edit").format(user_id))
    
def password_update(request, user_id):
    print "pw 1"
    result = User.objects.validate_passwords(request.POST, user_id)    
    if result==True: #password matched......        
        result = User.objects.update_password(request.POST['new_password'], user_id)        
        if result==True:
            messages.success(request, result)
            print "password updated"            
        else:
            messages.error(request,result)        
            print result
    else:
        messages.error(request, result)
        print result
    return redirect(("/users/{}/edit").format(user_id))


def update(request, user_id):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)        
        return redirect('/users/{}/edit'.format(user_id))

    user_to_update = User.objects.get(id=user_id)
    user_to_update.first_name = request.POST['first_name']
    user_to_update.last_name = request.POST['last_name']
    user_to_update.email = request.POST['email']
    user_to_update.save()
    return redirect('/users')


def show(request, user_id):
    record = User.objects.get(id=user_id)
    
    about_profile = {
        "name": "{} {}".format(str(record.first_name), str(record.last_name)),
        "first_name":record.first_name,
        "created_at": record.created_at ,
        "user_id": record.id ,
        "email": record.email ,
        "birth_date": record.birth_date ,
        "description": record.description        
    }
    ##thisSQL = Message.objects.raw("SELECT * FROM userd_Message")
    message_list = []
    comment_list = []
    print "request.session['user_id']:",request.session['user_id']
    messages_obj = Message.objects.filter(user_id=user_id)  # Calry'; messages......  
    print "user_id", user_id
    print "messages_obj: ",messages_obj
    print "messages_obj.count: ",messages_obj.count()    
    for message_obj in messages_obj: # has the name of the postee...
        message_poster_obj = User.objects.get(id=message_obj.muser_id)  # gets the name of the poster....
        print "message_obj.muser_id: ", message_obj.muser_id
        print "message_obj.user_id: ", message_obj.user_id
        print "message poster:", "{} {}".format(message_poster_obj.first_name, message_poster_obj.last_name)
        if (timezone.now() + timedelta(-7)) < message_obj.created_at:
            when = "{} ago".format(human(message_obj.created_at))
        else:      
            when = message_obj.created_at.strftime("%b %d, %Y")        
        print "when: ", when     

        record = {
            "name": "{} {}".format(message_poster_obj.first_name, message_poster_obj.last_name),
            "message": message_obj.message,            
            "when": when,#m.created_at.strftime("%b %d, %Y"),
            "message_id": message_obj.id,
            "muser_id": message_obj.id} # poster Id of message

        message_list.append(record)        
        comments_obj = Comment.objects.filter(message_id = message_obj.id)
        print "comments_obj: ", comments_obj
        print "comments_obj.count: ", comments_obj.count()
        for comment_obj in comments_obj:
            comment_poster_obj = User.objects.get(id=comment_obj.cuser_id) # gets person posting comment
            print "comment poster:", "{} {}".format(comment_poster_obj.first_name, comment_poster_obj.last_name)
            if timezone.now() + timedelta(-7) < message_obj.created_at:
                when = "{} ago".format(human(message_obj.created_at))
            else:      
                when = message_obj.created_at.strftime("%b %d, %Y")        
            print "when: ", when      

            record = {
                "name": "{} {}".format(comment_poster_obj.first_name, comment_poster_obj.last_name),
                "comment": comment_obj.comment,                
                "when": when,#c.created_at.strftime("%b %d, %Y"),
                "message_id": message_obj.id,
            }
            comment_list.append(record)

    print "message_list: ", len(message_list)
    print "comment_list: ", len(comment_list)

    ##these_comments = Comment.objects.filter(user_id=user_id)
    #for this in these_messages:
    #    print "messages: ", this.id, " - ", this.user_id, " - ", this.message
    #for this in these_comments:
    #    print "comments: ", this.id, " - ", this.user_id, " - ", this.user_id.first_name, " - ", this.message_id.message  
    return render(request, 'userd/show.html', {'user': about_profile, 'user_messages':message_list, 'user_comments':comment_list}) ########################## need from The Wall assignmentsssssssss

def post_message(request,user_id):
    result = Message.objects.post_this_message(request.POST, request.session['user_id'], user_id)
    print "post message", result            
    return redirect("/users/{}/show".format(user_id),request)

def post_comment(request,user_id, message_id):
    print "post comment"
    result = Message.objects.post_this_comment(request.POST, user_id, message_id)
    print "comment result: ", result
    print "post message", result         
    return redirect("/users/{}/show".format(user_id),request)

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/dashboard')

def userdbd(request):    
    return render(request,'userd\\userdbd.html')

def admindbd(request):
    
    return render(request,'userd\\admindbd.html')

def new(request):    
    return render(request, 'userd\\addnew.html')

def createNew(request):# validate registration, send to dbaase
    result = User.objects.registration_validate(request.POST)
    print "new result: ", result
    print "new type(result): ", type(result)
    if type(result) == list: # a list identifies that there are errors, else it is a dbase record.
        for err in result:
            messages.error(request, err)
        request.session['login'] = False
        return redirect('/')  #################################################### testing to see if redirect to login....
        return render(request,'userd\\addnew.html') # redirect back.....
    messages.success(request, "Successfully added!")    
    return redirect("/success/{}".format(result.id),{"user_id":result.id})#,result) # returns record of who is logged in...
