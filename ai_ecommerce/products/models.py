from django.conf import settings
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    tags = models.CharField(max_length=200, blank=True)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name
