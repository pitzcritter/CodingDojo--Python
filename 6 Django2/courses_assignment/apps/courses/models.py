from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['name']) < 5:
            errors.append("Name >= 5 characters")
        if len(post_data['desc']) < 15:
            errors.append("Description >= 15 characters")
        return errors

class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()