from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    date_added = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)  # Default value provided

    def __str__(self):
        return self.title
class Member(models.Model):
    name = models.CharField(max_length=200)
    member_id = models.CharField(max_length=50, unique=True)
    date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name