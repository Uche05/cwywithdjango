from django.contrib import admin

from .models import Availability, Booking, TimeOffRequest, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Availability)
admin.site.register(Booking)
admin.site.register(TimeOffRequest)
