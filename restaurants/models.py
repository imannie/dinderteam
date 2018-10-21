from django.db import models



# Create your models here.
class Restaurants_info(models.Model):
    name = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    rating = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    hold = models.CharField(max_length=300)
    selected = models.CharField(max_length=300,default="")