# This file will be used to redirect to different views as per the endpoint added to the url
from django.urls import path
from . import views # here '.' dit means from current directory

urlpatterns = [
    path('', views.index, name='index') # here while hitting the url without end point it will redirect to index.html which i have created as function inside views.py
]