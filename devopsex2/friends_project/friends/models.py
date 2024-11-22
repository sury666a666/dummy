from django.db import models # type: ignore

class Friend(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

