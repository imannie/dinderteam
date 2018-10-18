from django.shortcuts import render, redirect
import requests
import urllib.request 
import cv2
import numpy as np

header = {
    "Authorization":  "Bearer EgNHeojg_ryrKUYzlgCaPMXU7i60GOR-Yy1qxnoYvIDNM8OEq1bfq1a5cbuiExw94-oDF86cKIGfZI73iQoXsxZYndshHdSCeqUMjCi1C-KqdY1jA2Rkw5O4OQWwWnYx"
}
response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&location=oakland", headers=header)
data = response.json()

for info in data['businesses']:
    single = info["alias"]
    price = info["price"]
    rating = info["rating"]
    image = info["image_url"]

def index(request):
    data = str(rating)+"/5.0" 
    context= {
        
        "price":price,
        "name":single,
        "rating":data,
        "image":image,

    }
    return render(request, "../new_age/index.html", context)
