# books/models.py
from django.db import models # type: ignore

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    description = models.TextField()

    def __str__(self):
        return self.title
