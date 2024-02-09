"""This will keep the views"""

from django.shortcuts import render
from django.http import HttpResponse


def my_blog(request):
    """
    The views for the  project
    """
    return HttpResponse("Hello, Blog!")
