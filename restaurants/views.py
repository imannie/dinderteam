from django.shortcuts import render, redirect
import requests
import sqlite3
from .models import Restaurants_info
import random

def index(request):

    try:
        header = {
            "Authorization":  "Bearer EgNHeojg_ryrKUYzlgCaPMXU7i60GOR-Yy1qxnoYvIDNM8OEq1bfq1a5cbuiExw94-oDF86cKIGfZI73iQoXsxZYndshHdSCeqUMjCi1C-KqdY1jA2Rkw5O4OQWwWnYx"
        }   
        response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&location=oakland", headers=header)
    except IOError:
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
    seen = Restaurants_info.objects.get(name = got_one.name)
    seen.selected = 1
    seen.save()

    if request.method == "GET":
        print("thsi si carzy")
        g = request.POST.get('good')
        b = request.GET.get('bad')
        print(g)
        print(b)
        if  g:
            print("working?")
            update_good = Restaurants_info.objects.get(name = got_one.name)
            update_good.hold = 1
            update_good.save()
        elif b:
            print("?")
            update_bad = Restaurants_info.objects.get(name = got_one.name)
            update_bad.hold = 0
            update_bad.save()

    context = {
        "name":  got_one.name,
        "price": got_one.price,
        "rating":data,
        "image": got_one.image,

    }

   
    return render(request, "../new_age/index.html",context)


    
