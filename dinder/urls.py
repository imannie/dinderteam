
from django.contrib import admin
from django.urls import path
from restaurants import views

urlpatterns = [
    
    path('',views.index),
    path('index',views.index),
<<<<<<< HEAD
    # path('winner',views.winner),
=======
    path('swipe',views.swipe),
>>>>>>> 43434ed75b27e051af56d1c2d9272a9f05f0f0f4
]
