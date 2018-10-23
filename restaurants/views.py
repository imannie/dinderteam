from django.shortcuts import render, redirect
import requests
import sqlite3
from .models import Restaurants_info
import random
from django import forms
import glob
import os
from django.http import HttpResponse


# start of Jordan's drop-down code
dropdown_city= [
    ('Oakland', "Oakland"),
    ("San Francisco", "San francisco"),
    ("Alameda", "Alameda"),
    ("San Jose", "San Jose"),
    ("Daily City", "Daily City"),
    ("Berkeley", "Berkeley"),
    ("San Leandro", "San Leandro"),
    ("Hayward", "Hayward"),

]
dropdown_prices = [
    ("1", "$"),
    ("2", "$$"),
    ("3", "$$$"),
    ("4", "$$$$")
]

dropdown_food = [
    ('burger', 'Burger'),
    ('chinese', 'Chinese'),
    ("italian", "Italian"),
    ("japanese", "Japanese"),
    ("mexican", "Mexican"),
    ("thai", "Thai")
]

   

class FiltersCityForm(forms.Form):
    location = forms.ChoiceField(label="Pick a city", choices=dropdown_city)
    price = forms.ChoiceField(label="Price", choices=dropdown_prices) 
    alias = forms.ChoiceField(label="Food Type", choices=dropdown_food)
    


def homepage(request):
    
    form  = FiltersCityForm(request.POST)
    
    if request.method == 'POST':
       
        # Fill out form with thedata they provide
        form_city = FiltersCityForm(request.POST)
        if form_city.is_valid():
            location = form_city.cleaned_data['location']
            price = form_city.cleaned_data['price']
            alias = form_city.cleaned_data['alias']
    
            print(location, price, alias)

            header = {
            "Authorization":  "Bearer EgNHeojg_ryrKUYzlgCaPMXU7i60GOR-Yy1qxnoYvIDNM8OEq1bfq1a5cbuiExw94-oDF86cKIGfZI73iQoXsxZYndshHdSCeqUMjCi1C-KqdY1jA2Rkw5O4OQWwWnYx"
            }
            response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&radius=16093&location=" + location + "&price=" + price + "&categories=" + alias, headers=header)
            data = response.json()


            if request.session.get('has_visited'):
              for item in data['businesses']:
                  print("working")
                  restaurant = Restaurants_info.objects.create(
                      name = item['name'],
                      price = item['price'],
                      rating = item['rating'],
                      image = item['image_url'], 
                      # session_key=request.session_key,
                  )
              request.session['has_visited'] = True

        return redirect('/swipe')
    else:
        # Make blank, empty form, for them to use
        form_city= FiltersCityForm()
    
        context = {
        
            'form_city': form_city,
        
        }
    


        return render(request, "homepage.html", context)

def details(request):
    # form  = FiltersForm(request.POST)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         return redirect("/swipe/")
    context = {
        # 'form': form,
        
     }

    return render(request, "details.html", context)


# end of Jordan's drop-down code



def swipe(request):
    # header = {
    #     "Authorization":  "Bearer EgNHeojg_ryrKUYzlgCaPMXU7i60GOR-Yy1qxnoYvIDNM8OEq1bfq1a5cbuiExw94-oDF86cKIGfZI73iQoXsxZYndshHdSCeqUMjCi1C-KqdY1jA2Rkw5O4OQWwWnYx"
    # }   
    # response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&location=oakland", headers=header)
    # data = response.json()

    # if request.session.get('has_visited'):
    #     for item in data['businesses']:
    #         restaurant = Restaurants_info.objects.create(
    #             name = item['name'],
    #             price = item['price'],
    #             rating = item['rating'],
    #             image = item['image_url'], 
    #         )
    #     request.session['has_visited'] = True

    got_one = Restaurants_info.objects.order_by('?')[0]
    data = str(got_one.rating)+"/5.0"
    seen = Restaurants_info.objects.get(name = got_one.name)
    seen.selected = 1
    seen.save()

    g = request.GET.get('good')
    b = request.GET.get('bad')
    res_id = request.GET.get("res_id")
    if g:
      print("good")
      update_good = Restaurants_info.objects.get(id = res_id)
      update_good.hold = 1
      update_good.save()
    elif b:
      print("bad")
      update_bad = Restaurants_info.objects.get(id = res_id)
      update_bad.hold = 0
      update_bad.save()

    context = {
        "name":  got_one.name,
        "price": got_one.price,
        "rating":data,
        "image": got_one.image,
        "res_id":got_one.id,

    }

   
    return render(request, "swipe.html",context)