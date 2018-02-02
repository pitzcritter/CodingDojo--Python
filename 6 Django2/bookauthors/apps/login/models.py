from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime, date, time
#from time import strptime, strftime  nused in birtday...
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z ]+$') # with space
##NAME_REGEX = re.compile(r'^[A-Za-z]\w+$') # without space
#BDAY_REGEX = re.compile(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$')


class UserManager(models.Manager):
    
    def validate_login(self, post_data):
        errors = []
        # check DB for post_data['email']
        if len(self.filter(email=post_data['email'])) > 0:
            # check this user's password
            user = self.filter(email=post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('email/password incorrect')
        else:
            errors.append('email/password incorrect')

        if errors:
            return (False,errors)
        return (True,user)

    # def books_reviewed(self):
    #     return self.model.reviews_left.all().values('book').distict()

    def validate_registration(self, post_data):
        errors = []        
        # check length of name fields
        if len(post_data['name']) < 2 or len(post_data['alias']) < 2:
            errors.append("Name fields must be at least 3 characters.")
        #if len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2:
        #    errors.append("Name fields must be at least 3 characters.")
        # check length of name password
        if len(post_data['password']) < 8:
            errors.append("Password must be at least 8 characters.")
        # check name fields for letter characters            
        print "name: ",post_data['name']
        print "regex: ",re.match(NAME_REGEX, post_data['name'])
        if not re.match(NAME_REGEX, post_data['name']):
            errors.append('Name fields must be letter characters only.')
        # check emailness of email
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("Invalid email.")
        # check birthday        
        #if len(post_data['birth_date']) < 6:
        #    errors.append("birth date empty")    
        #elif not re.match(BDAY_REGEX, post_data['birth_date']):
        #    errors.append("invalid birth date")
        #else:
        #    if strptime(post_data['birth_date'],'%Y-%m-%d') >= strptime(str(date.today()),'%Y-%m-%d'):                
        #        errors.append("Birth date too high!")

        # check uniqueness of email
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("Email already in use.")
        # check password == password_confirm
        if post_data['password'] != post_data['password_confirm']:
            errors.append("Passwords don't match.")

        if not errors:
            # make our new user
            # hash password
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                name=post_data['name'],
                alias=post_data['alias'],
                email=post_data['email'],
                password=hashed
            )
            return (True,new_user)
        return (False,errors)


class User(models.Model):
    name = models.CharField(max_length=100)
    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)    
    alias = models.CharField(max_length=100)
    #birth_date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.email