
from django.contrib import admin
from django.urls import path
from restaurants import views

urlpatterns = [
    
    path('',views.homepage),
    # path('swipe',views.index),
    # path('winner',views.winner),
]
