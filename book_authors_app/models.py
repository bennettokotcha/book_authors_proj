from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # authors = [a list of authors this Book has]
class Author(models.Model):
    books = models.ManyToManyField(Book, related_name='authors')
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
