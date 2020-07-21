"""
The urls file for the gamestats django app.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
