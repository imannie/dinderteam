from django.db import models


# Create your models here.
class Restaurants_info(models.Model):
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    rating = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    hold = models.CharField(max_length=300)
    selected = models.CharField(max_length=300,default="0")
    url = models.CharField(max_length=1000,default="") 
    phone = models.CharField(max_length=300,default="")
    address = models.CharField(max_length=500, default="")
    session_key = models.CharField(max_length=300,null=True)
