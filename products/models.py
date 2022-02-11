from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()  # forget the () there -- did that in another migration
    image_url = models.CharField(max_length=2083) #as image url from google or web can have very long url
    
class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

