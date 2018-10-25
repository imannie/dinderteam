from django.shortcuts import render, redirect
import requests
import sqlite3
from .models import Restaurants_info
import random
from django import forms
import glob
import os
from django.conf import settings
from django.http import HttpResponse
from django import forms
from django.contrib import messages

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

            Restaurants_info.objects.filter(session_key=request.session.session_key).delete()
            #Michael added this to delete the current sessions existing data if we come back to home page

            header = {
            "Authorization":  "Bearer EgNHeojg_ryrKUYzlgCaPMXU7i60GOR-Yy1qxnoYvIDNM8OEq1bfq1a5cbuiExw94-oDF86cKIGfZI73iQoXsxZYndshHdSCeqUMjCi1C-KqdY1jA2Rkw5O4OQWwWnYx"
            }
            response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&radius=16093&location=" + location + "&price=" + price + "&categories=" + alias, headers=header)
            data = response.json()
            request.session['count'] = 0 
           
            for item in data['businesses']:
                restaurant = Restaurants_info.objects.create(
                    name = item['name'],
                    price = item['price'],
                    rating = item['rating'],
                    image = item['image_url'], 
                    url = item['url'], 
                    phone = item['phone'], 
                    address = item["location"]['address1'], 
                    session_key = request.session.session_key,
                    selected = 0;
                )

            if data["total"] == 0:
                messages.warning(request, 'No Restaurants Matching Search Criteria')

                return redirect('/')

            # seen = Restaurants_info.objects.filter(name = got_one.name).first()
            # seen.selected = 0
            # seen.save()

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
    context = {}

    return render(request, "details.html", context)


def swipe(request):
  
    key_check = request.session.session_key

    relevant_restaurants = Restaurants_info.objects.filter(session_key = key_check)
    if relevant_restaurants.count() < 1:
        messages.warning(request, 'No Restaurants in Database')
        
        return redirect('/')

    got_one = relevant_restaurants.filter(selected = "0").order_by('?')[0]
    seen = Restaurants_info.objects.filter(name = got_one.name).first()
    seen.selected = 1
    seen.save()


    good = request.GET.get('good')
    bad = request.GET.get('bad')
    res_id = request.GET.get("res_id")
    if good: 
        update_good = Restaurants_info.objects.get(id = res_id)
        update_good.hold = 1
        update_good.save()
        request.session['count'] = request.session['count'] + 1
    elif bad: 
        update_bad = Restaurants_info.objects.get(id = res_id)
        update_bad.hold = 0
        update_bad.save()

#TODO: change to count the # for rows in hold with 1 
    if request.session['count'] == 4:
        lets_chose(request)

    data = str(got_one.rating)+"/5.0"
    context = {
        "name":  got_one.name,
        "price": got_one.price,
        "rating":data,
        "image": got_one.image,
        "res_id":got_one.id,
        "phone":got_one.phone,
        "address":got_one.address,
        "url":got_one.url,
    }
    return render(request, "swipe.html",context)



def lets_chose(request):
#      _____ _   _ ___ _   _  ____ ____    _____ ___    ____   ___
# |_   _| | | |_ _| \ | |/ ___/ ___|  |_   _/ _ \  |  _ \ / _ \
#   | | | |_| || ||  \| | |  _\___ \    | || | | | | | | | | | |
#   | | |  _  || || |\  | |_| |___) |   | || |_| | | |_| | |_| |
#   |_| |_| |_|___|_| \_|\____|____/    |_| \___/  |____/ \___/

   #we should add a start over button that redirects to the swipe page or to home
   # we should also give them the ability to see the rest of the list they swiped yes on  

#    __        _____       _
# \ \      / / _ \ _ __| | _____
#  \ \ /\ / / | | | '__| |/ / __|
#   \ V  V /| |_| | |  |   <\__ \
#    \_/\_/  \___/|_|  |_|\_\___/

    #this prints out random restaurant
    yes_swipe= Restaurants_info.objects.all().filter(hold ="1").order_by('?')[0]
    data = str(yes_swipe.rating)+"/5.0"
    print("we are here")
    context = {
        "name":  yes_swipe.name,
        "price": yes_swipe.price,
        "rating":data,
        "image": yes_swipe.image,
        "res_id":yes_swipe.id,
        "phone":yes_swipe.phone,
        "address":yes_swipe.address,
        "url":yes_swipe.url,
    }
    return render(request, "swipe.html",context)
   
