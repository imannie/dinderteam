from django.shortcuts import render, redirect
import requests
import sqlite3
from django import forms
import glob
import os
from django.http import HttpResponse

# holder = []
# all_html_files = glob.glob("content/*.html")
# for single in all_html_files:
#     file_name = os.path.basename(single)
#     name_only, extension = os.path.splitext(file_name)
#     holder.append(name_only)


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

print(names)
dropdown_choices= [
    (name, "name")

]


# class FiltersForm(forms.Form):
#     # city = forms.CharField(label="Food Type", widget=forms.Select(choices=dropdown_choices[1]))
#     # price = forms.CharField(label="Food Type", widget=forms.Select(choices=dropdown_choices[1]))
#     # rating = forms.CharField(label="Food Type", widget=forms.Select(choices=dropdown_choices[2]))
#     food_type = forms.CharField(label="Food Type", widget=forms.Select(choices=names))
   



def homepage(request):
    # form  = FiltersForm(request.POST)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         return redirect("/swipe/")
    context = {
        # 'form': form,
        
     }

    return render(request, "homepage.html", context)


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