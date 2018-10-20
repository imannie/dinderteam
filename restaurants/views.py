from django.shortcuts import render, redirect
import requests
import sqlite3
from .models import Restaurants_info
import random

def index(request):
    header = {
        "Authorization":  "Bearer EgNHeojg_ryrKUYzlgCaPMXU7i60GOR-Yy1qxnoYvIDNM8OEq1bfq1a5cbuiExw94-oDF86cKIGfZI73iQoXsxZYndshHdSCeqUMjCi1C-KqdY1jA2Rkw5O4OQWwWnYx"
    }   
    response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&location=oakland", headers=header)
    data = response.json()

    if request.session.get('has_visited'):
        for item in data['businesses']:
            restaurant = Restaurants_info.objects.create(
                name = item['name'],
                price = item['price'],
                rating = item['rating'],
                image = item['image_url'], 
            )
        request.session['has_visited'] = True

    got_one = Restaurants_info.objects.order_by('?')[0]
    data = str(got_one.rating)+"/5.0"

    context = {
        "name":  got_one.name,
        "price": got_one.price,
        "rating":data,
        "image": got_one.image,

    }

   
    return render(request, "../new_age/index.html",context)


    