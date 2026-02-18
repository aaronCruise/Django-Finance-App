from django.contrib import admin
from django.urls import path

# Importing views from views.py
from .views import stock_data

urlpatterns = [
    path('', stock_data),
]
