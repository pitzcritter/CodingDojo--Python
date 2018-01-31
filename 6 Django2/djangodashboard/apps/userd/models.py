from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime, date, time
from time import strptime
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')
BDAY_REGEX = re.compile(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$')


class LoginManager(models.Manager):
    def validate_passwords(self, post_data, user_id):
        if post_data['new_password']=="":
            return "new password empty."
        if post_data['confirm_password']=="":
            return "confirm password empty."
        #if post_data['current_password']=="":
        #    return "current password empty."

        if len(post_data['new_password'])<8:
            return "new password needs to be > 7 characters"
        if len(post_data['confirm_password'])<8:
            return "confirm password needs to be > 7 characters"

        if not post_data['new_password'] == post_data['confirm_password']:
            return "new passwords donot match!"

        #if post_data['new_password']==post_data['current_password']:
        #    return "new password cannot match old passsword"

        try: 
            user = User.objects.get(id=user_id)
        except:
            print "Database record not found"
            return "Database record not found"
        print "pw clean"
        return True # bcrypt.checkpw(post_data['current_password'].encode(), user.password.encode())

    def update_password(self, new_password, user_id):        
        try:
            record = User.objects.get(id=user_id)
        except:            
            return 'Error: password database object not successful.'
        try:
            record.password = bcrypt.hashpw(post_data['new_password'].encode(), bcrypt.gensalt())            
        except:
            return 'Error: Database passord NOT updated'
        record.save()        
        return True

    def login_validate(self, post_data):
        errors = []
        try: 
            user = self.get(email=post_data['email'])#[0]
        #if len(self.filter(email=post_data['email'])) > 0:
        #if user.count() > 0:
        except:
            errors.append('email not exist')
            print "return errors:", errors
            return errors        

        if bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
            print "return user:", user
            return user
        else:
            errors.append('email &/or password incorrect')
            print "return errors:", errors
            return errors        
        #return user # not needed.....

    def registration_validate(self, post_data):
        errors = []
        if post_data['first_name']=='' or post_data['last_name']=='':
            errors.append("name is empty")    
        elif len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2:
            errors.append("name fields must be at least 3 characters")    
        elif not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append('name fields must be letter characters only')    

        if post_data['email']=='':
            errors.append("email empty")    
        elif not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("invalid email")
        elif len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("email already in use")

        if post_data['password']=='':
            errors.append("password empty")                
        elif len(post_data['password']) < 8:
            errors.append("password > 8 characters")
        elif post_data['password'] != post_data['confirm_password']:
            errors.append("passwords do not match")
        
        if post_data['birth_date']=='':
            errors.append("birth date empty")    
        elif not re.match(BDAY_REGEX, post_data['birth_date']):
            errors.append("invalid birth date")
        else:
            if strptime(post_data['birth_date'],'%Y-%m-%d') >= strptime(str(date.today()),'%Y-%m-%d'):                
                errors.append("Birth date too high!")
        if not errors:
            hash = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt())#bcrypt.gensalt(5))

            # User.objects.create(first_name="first",last_name="last",birth_date='2018-1-1',email="B24@D.com",password="frfe",user_level=UserLevel.objects.get(user_level=1))
            if self.filter(user_level=2).count() > 0:
                userlevel=UserLevel.objects.get(level=1)
                #User.objects.create(first_name=post_data['first_name'],last_name=post_data['last_name'],birth_date=post_data['birth_date'],email=post_data['email'],password=hash,user_level=UserLevel.objects.get(user_level=1))
            else:                
                userlevel=UserLevel.objects.get(level=9)
                #3User.objects.create(first_name=post_data['first_name'],last_name=post_data['last_name'],birth_date=post_data['birth_date'],email=post_data['email'],password=hash,user_level=UserLevel.objects.get(user_level=9))
                        
            new_user = self.create(
                first_name=post_data['first_name'],
                last_name=post_data['last_name'],
                birth_date=post_data['birth_date'],
                email=post_data['email'],
                password=hash,
                user_level=userlevel)
            return new_user
        return errors

    def edit_validate(self, post_data, user_id):
        errors = []
        print "post_data: ", post_data
        print "post_data['first_name'] 1 : ", post_data['first_name']
        print "post_data['last_name']: ", post_data['last_name']
        if post_data['first_name']=='' or post_data['last_name']=='':
            errors.append("name is empty")    
        elif len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2:
            errors.append("name fields must be at least 3 characters")    
        elif not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append('name fields must be letter characters only')    

        if post_data['email']=='':
            errors.append("email empty")    
        elif not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("invalid email")
        
        if post_data['birth_date']=='':
            errors.append("birth date empty")    
        elif not re.match(BDAY_REGEX, post_data['birth_date']):
            errors.append("invalid birth date")
        else:
            if strptime(post_data['birth_date'],'%Y-%m-%d') >= strptime(str(date.today()),'%Y-%m-%d'):                
                errors.append("Birth date too high!")
        if not errors:    
            print "update record"        
            record = User.objects.get(id=user_id)
            if not record.first_name == post_data['first_name']:
                record.first_name = post_data['first_name']
                print "updated first_name"
            if record.last_name == post_data['last_name']:
                record.last_name = post_data['last_name']
                print "updated last_name"
            if not record.birth_date == post_data['birth_date']:
                record.birth_date = post_data['birth_date']
                print "updated birth_date"
            if not record.email == post_data['email']:
                record.email = post_data['email']
                print "updated email"
            record.save()
            return True
        return errors

    def isAdmin(self,request):
        #thisUser = User.objects.get(id=request.session['user_id'])
        thisUser = User.objects.get(id=request.session['user_id'])
        print "   thisUser.user_level.level: ", thisUser.user_level.level
        print "   thisUser.user_level.usertext: ", thisUser.user_level.usertext
        print "   thisUser.email: ", thisUser.email
        if thisUser.user_level.usertext == 'Admin':
            return True
        else:
            return False


class DiscussionManager(models.Manager):
    
    def post_this_message(self, post_data, login_id, user_id):
        new_message = self.create(            
            message = post_data['message'],    
            muser_id = login_id, #gives the post
            user_id = user_id) # recieves the post
        return new_message

    def post_this_comment(self, post_data, user_id, message_id):
        print "commenting"
        new_comment = Comment.objects.create(
            comment = post_data['comment'],    
            cuser_id = user_id, # gives the comment            
            message_id = message_id)
        return new_comment


class UserLevel(models.Model):
    level = models.IntegerField(verbose_name=None)
    usertext = models.CharField(max_length=255)
    # users from join


# https://docs.djangoproject.com/en/2.0/ref/forms/fields/#built-in-field-classes
#  models.IntegerField(default=0) 
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)    
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #user_level = models.PositiveSmallIntegerField(verbose_name=None)
    user_level = models.ForeignKey(UserLevel, related_name = "users")
    description = models.TextField(null=True, blank=True)
    ##blog = models.ForeignKey(Blog, related_name = "comments")    
    objects = LoginManager()
    def __str__(self):
        return self.email # returns email.....

class Message(models.Model):
    user = models.ForeignKey(User, related_name = "messages")# person recieving message.
    muser_id=models.IntegerField(verbose_name=None) # person posting message.
    message=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = DiscussionManager()

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name = "message_comments")#message receiving comment.
    cuser = models.ForeignKey(User, related_name = "user_comments") #person recieving comment.
    #cuser_id=models.IntegerField(verbose_name=None) # person posting comment.
    comment = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
