
from django.contrib import admin
from django.urls import path
from restaurants import views

urlpatterns = [
    
    path('',views.index),
    path('index',views.index),
    path('swipe',views.swipe),
]
