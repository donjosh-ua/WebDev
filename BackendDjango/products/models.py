from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    img_route = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
