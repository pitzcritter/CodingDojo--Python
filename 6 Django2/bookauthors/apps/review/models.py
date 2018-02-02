from __future__ import unicode_literals
from ..login.models import User # User dbase table imported from login app...............
from django.db import models


class ReviewManager(models.Manager):
    def validate_review(self, post_data):
        errors = []

        if len(post_data['title']) < 1 or len(post_data['review']) < 1:
            errors.append('fields are required')
        if not "author" in post_data and len(post_data['new_author']) < 3:
            errors.append('new author names must > 2 characters')

        if "author" in post_data and len(post_data['new_author']) > 0 and len(post_data['new_author']) < 3:
            errors.append('new author names must be > 2 characters')
        if not int(post_data['rating']) > 0 or not int(post_data['rating']) <= 5:
            errors.append('rating invalid')
        return errors

    def create_review(self, this_record, user_id):
        # retrive or create author
        the_author = None
        if len(this_record['new_author']) < 1:
            the_author = Author.objects.get(id=int(this_record['author']))
        else:
            the_author = Author.objects.create(name=this_record['new_author'])
        # retirive or create book
        the_book = None
        if not Book.objects.filter(title=this_record['title']):
            the_book = Book.objects.create(
                title=this_record['title'], author=the_author
            )
        else:
            the_book = Book.objects.get(title=this_record['title'])
        # returns a Review object
        return self.create(
            review = this_record['review'],
            rating = this_record['rating'],
            book = the_book,
            reviewer = User.objects.get(id=user_id)
        )
    
     #	Review.objects.create(book=Book.objects.get(id=1), author="@#$$@) 
    def recent_and_allelse(self, this_number):
        '''                
         raw query:  https://docs.djangoproject.com/en/2.0/topics/db/sql/
         for p in Person.objects.raw('SELECT * FROM myapp_person'):
            print(p)
        
           below returns tuple of (most recent n records: all records beyond record n)
        '''
        return (self.all().order_by('-created_at')[:this_number], self.all().order_by('-created_at')[this_number:])

class Author(models.Model): # few
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model): # more
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books")  # foreign key
    def __str__(self):
        return self.title

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()

    book = models.ForeignKey(Book, related_name="reviews")    
    reviewer = models.ForeignKey(User, related_name="reviews_left")
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
    def __str__(self):
        return "Book: {}".format(self.book.title)