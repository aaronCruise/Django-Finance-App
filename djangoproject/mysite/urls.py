""" Create a path to the html template of the home page."""
from django.contrib import admin
from django.urls import path
from .views import stock_data

urlpatterns = [
    path('', stock_data),
]
