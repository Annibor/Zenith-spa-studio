"""This will keep the views"""

from django.shortcuts import render



def starting_page(request):
    """
    The startpage views
    """
    return render(request, 'home/index.html')
