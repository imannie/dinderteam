from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from django import forms
from .models import Restaurants_info
import requests
import sqlite3

dropdown_city= [
    ('Oakland', "Oakland"),
    ("San Francisco", "San francisco"),
    ("Alameda", "Alameda"),
    ("San Jose", "San Jose"),
    ("Daly City", "Daly City"),
    ("Berkeley", "Berkeley"),
    ("San Leandro", "San Leandro"),
    ("Hayward", "Hayward"),
    ("Santa Monica", "Santa Monica"),

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

            #deletes the users previous queries 
            Restaurants_info.objects.filter(session_key=request.session.session_key).delete()

            header = {
            "Authorization":  "Bearer EgNHeojg_ryrKUYzlgCaPMXU7i60GOR-Yy1qxnoYvIDNM8OEq1bfq1a5cbuiExw94-oDF86cKIGfZI73iQoXsxZYndshHdSCeqUMjCi1C-KqdY1jA2Rkw5O4OQWwWnYx"
            }
            response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&radius=16093&location=" + location + "&price=" + price + "&categories=" + alias, headers=header)
            data = response.json()
           
            for item in data['businesses']:
                addy = item["location"]['address1']
                city = item["location"]['city']
                state = item["location"]['state']
                zip_code = item["location"]['zip_code']
                address = addy+", "+city+", "+state+" "+zip_code
                restaurant = Restaurants_info.objects.create(
                    name = item['name'],
                    price = item['price'],
                    rating = item['rating'],
                    image = item['image_url'], 
                    url = item['url'], 
                    phone = item['phone'], 
                    address = address, 
                    session_key = request.session.session_key,
                )
                #checks to make sure the params have found something and if not responds with error and sends user to homepage
            if data["total"] == 0:
                messages.warning(request, 'No Restaurants Matching Search Criteria')
                return redirect('/')

        return redirect('/swipe')
    else:
        # Make blank, empty form, for them to use
        form_city= FiltersCityForm()
    
        context = {
            'form_city': form_city,
        }
        return render(request, "homepage.html", context)

def swipe(request):
  
    key_check = request.session.session_key
    
    relevant_restaurants = Restaurants_info.objects.filter(session_key = key_check)
   # checks to make sure db has something in it 
    if relevant_restaurants.count() < 1:
        messages.warning(request, 'No Restaurants in Database') 
        return redirect('/')

    # makes sure we didnt run out of options to display
    checkTheList = relevant_restaurants.filter(selected = "0")
    if checkTheList.count() == 0:
        print("okay")
        return redirect("/winner")

    #selects an object from the db at random and marks selected to know we have seen it 
    got_one = checkTheList.order_by('?')[0]
    seen = Restaurants_info.objects.filter(name = got_one.name).first()
    seen.selected = 1
    seen.save()

    #in case duplicates exist - this makes sure they get seen as well
    all_seen = Restaurants_info.objects.all().filter(name = got_one.name).last()
    all_seen.selected = 1
    all_seen.save()

#if an object is liked vs disliked -- res_id used to make sure we are updating the correct object
    good = request.GET.get('good')
    bad = request.GET.get('bad')
    res_id = request.GET.get("res_id")
    if good: 
        update_good = Restaurants_info.objects.get(id = res_id)
        update_good.hold = 1
        update_good.save()
    elif bad: 
        update_bad = Restaurants_info.objects.get(id = res_id)
        update_bad.hold = 0
        update_bad.save()


    checkCount = Restaurants_info.objects.all().filter(hold = "1",session_key = key_check).count()
    print("this is the count",checkCount)
    if checkCount == 4:
        return redirect("winner/")

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
    key_check = request.session.session_key
    
    yes_swipe = Restaurants_info.objects.all().filter(hold ="1", session_key = key_check).order_by('?')[0]
    data = str(yes_swipe.rating)+"/5.0"
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
    return render(request, "winner.html",context)
   
