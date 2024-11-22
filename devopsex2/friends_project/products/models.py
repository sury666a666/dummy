# products/models.py
from django.db import models # type: ignore

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
