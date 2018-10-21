from django.shortcuts import render, redirect
import requests
import sqlite3
from django import forms
import glob
import os
from django.http import HttpResponse




header = {
    "Authorization":  "Bearer EgNHeojg_ryrKUYzlgCaPMXU7i60GOR-Yy1qxnoYvIDNM8OEq1bfq1a5cbuiExw94-oDF86cKIGfZI73iQoXsxZYndshHdSCeqUMjCi1C-KqdY1jA2Rkw5O4OQWwWnYx"
}
response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&location=oakland", headers=header)
data = response.json()

names = []
for info in data['businesses']:
    name = info["alias"]
    price = info["price"]
    rating = info["rating"]
    image = info["image_url"]
    names.append(name)


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
    ("one_dollar", "$"),
    ("two_dollar", "$$"),
    ("three_dollar", "$$$"),
    ("four_dollar", "$$$$")
]

dropdown_food = [
    ('Burger', 'Burger'),
    ('Chinese', 'Chinese'),
    ("Italian", "Italian"),
    ("Japanese", "Japanese"),
    ("Mexican", "Mexican"),
    ("Thai", "Thai")
]

   

class FiltersCityForm(forms.Form):
    city = forms.ChoiceField(label="Pick a city", choices=dropdown_city)
    price = forms.ChoiceField(label="Price", choices=dropdown_prices) 
    food = forms.ChoiceField(label="Food Type", choices=dropdown_food)
    


def homepage(request):
    form  = FiltersCityForm(request.POST)
    if request.method == 'POST':
        # Fill out form with thedata they provide
        form_city = FiltersCityForm(request.POST)
    else:
        # Make blank, empty form, for them to use
        form_city= FiltersCityForm()
    
    context = {
       
        'form_city': form_city,
       
     }
    


    return render(request, "homepage.html", context)







def swipe(request):
    # form  = FiltersForm(request.POST)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         return redirect("/swipe/")
    context = {
        # 'form': form,
        
     }

    return render(request, "swipe.html", context)

def details(request):
    # form  = FiltersForm(request.POST)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         return redirect("/swipe/")
    context = {
        # 'form': form,
        
     }

    return render(request, "details.html", context)


# def index(request):

#     if request.method == "POST":

#         user = User.objects.create(
#             name=name,
#             price=price,
#             rating=last_name,
#             image=password,
#             )

#         user.save()

#     if request.method == "post":
#         hold = 1
#         db = sqlite3.connect('db.sqlite3')
#         cursor = db.cursor()
#         cursor.execute('''INSERT INTO restaurants_restaurants_info(name, price, rating, image, hold)
#                     VALUES(?,?,?,?,?)''', (name, price, rating, image, hold))   
#         db.commit()
#         db.close()

#     data = str(rating)+"/5.0" 
#     context= {
        
#         "price":price,
#         "name":name,
#         "rating":data,
#         "image":image,

#     }
#     return render(request, "../new_age/index.html", context)


# '''
# The Winner code should pick the random winner from the maybe_list
# and display that resturant info, as read from the SQL database.
# '''
# def winner(request): 
#   context= {
      
#     "price":'price from SQLite (not implemented)',
#     "name":'name from SQLite (not implemented)',
#     "rating":'rating from SQLite (not implemented)',
#     "image": 'https://via.placeholder.com/350x350',

#   }
#   return render(request, "../new_age/winner.html", context)



# from .models import Restaurants_info
# import random

# def index(request):
#     header = {
#         "Authorization":  "Bearer EgNHeojg_ryrKUYzlgCaPMXU7i60GOR-Yy1qxnoYvIDNM8OEq1bfq1a5cbuiExw94-oDF86cKIGfZI73iQoXsxZYndshHdSCeqUMjCi1C-KqdY1jA2Rkw5O4OQWwWnYx"
#     }   
#     response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&location=oakland", headers=header)
#     data = response.json()

#     if request.session.get('has_visited'):
#         for item in data['businesses']:
#             restaurant = Restaurants_info.objects.create(
#                 name = item['name'],
#                 price = item['price'],
#                 rating = item['rating'],
#                 image = item['image_url'], 
#             )
#         request.session['has_visited'] = True

#     got_one = Restaurants_info.objects.order_by('?')[0]
#     data = str(got_one.rating)+"/5.0"

#     context = {
#         "name":  got_one.name,
#         "price": got_one.price,
#         "rating":data,
#         "image": got_one.image,

#     }

   
#     return render(request, "../new_age/index.html",context)


    
