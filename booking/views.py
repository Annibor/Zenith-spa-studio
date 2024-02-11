from django.shortcuts import render

# Create your views here.
def booking_page(request):
    """
    The startpage views
    """
    return render(request, 'booking/booking.html')