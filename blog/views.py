from django.shortcuts import render
from django.views import generic

from .models import Availability, Booking, TimeOffRequest, UserProfile


# Create your views here.
class AvailabilityListView(generic.ListView):
    model = Availability
    #template_name = 'availability_list.html'