"""
The apps file for the gamestats django app.
"""
from django.http import HttpResponse


def index(request):
    """
    Temporary index function for urls.
    """
    return HttpResponse('Hello, world. You are now at the gamestats app!')
