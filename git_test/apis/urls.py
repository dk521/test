from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('customers/', CustomerList.as_view()),    
    
]
