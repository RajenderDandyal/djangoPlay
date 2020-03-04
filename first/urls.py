from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile', views.profile),
    path('home', views.home),
    path('add', views.add),
    path('addPost', views.addPost),

]