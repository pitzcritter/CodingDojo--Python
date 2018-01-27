from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime, date, time
from time import strptime
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')
#BDAY_REGEX = re.compile(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$')
BDAY_REGEX = re.compile(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$')

# Create your models here.
class LoginManager(models.Manager):
    def login_validate(self, post_data):
        errors = []
        if len(self.filter(email=post_data['email'])) > 0:
            # check this user's password
            user = self.filter(email=post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('email &/or password incorrect')
        else:
            errors.append('email &/or password incorrect')

        if errors:
            return errors
        this = self.get(email=post_data['email'])        
        return this

    def registration_validate(self, post_data):
        print "V1"
        errors = []    
        if len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2:
            errors.append("name fields must be at least 3 characters")    
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append('name fields must be letter characters only')    
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("invalid email")
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("email already in use")
        if len(post_data['password']) < 8:
            errors.append("password > 8 characters")
        if post_data['password'] != post_data['confirm_password']:
            errors.append("passwords do not match")
        print "V2"
        if not re.match(BDAY_REGEX, post_data['birth_date']):
            errors.append("invalid birth date")
        else:
            if strptime(post_data['birth_date'],'%Y-%m-%d') >= strptime(str(date.today()),'%Y-%m-%d'):
                print post_data['birth_date'], ">=", date.today(),"!!!!!!!!!!!"
                errors.append("Birth date too high!")
        print "V3"
        if not errors:
            hash = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt())#bcrypt.gensalt(5))
            new_user = self.create(
                first_name=post_data['first_name'],
                last_name=post_data['last_name'],
                birth_date=post_data['birth_date'],
                email=post_data['email'],
                password=hash)
            return new_user
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #birth_date = models.CharField(max_length=10)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    objects = LoginManager()
    def __str__(self):#????????????????????????
        return self.email
