from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('series-tutorial/', views.tutorial_series),
    path('individual-tutorial/', views.individual_tutorial)
]

