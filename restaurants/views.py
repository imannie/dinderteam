from django.shortcuts import render, redirect
import requests
import sqlite3

header = {
    "Authorization":  "Bearer EgNHeojg_ryrKUYzlgCaPMXU7i60GOR-Yy1qxnoYvIDNM8OEq1bfq1a5cbuiExw94-oDF86cKIGfZI73iQoXsxZYndshHdSCeqUMjCi1C-KqdY1jA2Rkw5O4OQWwWnYx"
}
response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&location=oakland", headers=header)
data = response.json()

for info in data['businesses']:
    name = info["alias"]
    price = info["price"]
    rating = info["rating"]
    image = info["image_url"]
def index(request):

    # if request.method == "POST":

    #     user = User.objects.create(
    #         name=name,
    #         price=price,
    #         rating=last_name,
    #         image=password,
    #         )

    #     user.save()

    if request.method == "post":
        hold = 1
        db = sqlite3.connect('db.sqlite3')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO restaurants_restaurants_info(name, price, rating, image, hold)
                    VALUES(?,?,?,?,?)''', (name, price, rating, image, hold))   
        db.commit()
        db.close()

    data = str(rating)+"/5.0" 
    context= {
        
        "price":price,
        "name":name,
        "rating":data,
        "image":image,

    }
    return render(request, "../Newlook/index.html", context)


def swipe(request):
  # This is a temporary copy of the index code above, Rudy trying to make
  # this work with the new swiper.html page. 
    if request.method == "post":
        hold = 1
        db = sqlite3.connect('db.sqlite3')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO restaurants_restaurants_info(name, price, rating, image, hold)
                    VALUES(?,?,?,?,?)''', (name, price, rating, image, hold))   
        db.commit()
        db.close()

    data = str(rating)+"/5.0" 
    context= {
        
        "price":price,
        "name":name,
        "rating":data,
        "image":image,

    }
    return render(request, "../Newlook/swipe.html", context)


'''
The Winner code should pick the random winner from the maybe_list
and display that resturant info, as read from the SQL database.
'''
def winner(request): 
  context= {
      
    "price":'price from SQLite (not implemented)',
    "name":'name from SQLite (not implemented)',
    "rating":'rating from SQLite (not implemented)',
    "image": 'https://via.placeholder.com/350x350',

  }
  return render(request, "../new_age/winner.html", context)