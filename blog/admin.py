from django.contrib import admin

from .models import Availability, Booking, TimeOffRequest, User

# Register your models here.
admin.site.register(User)
admin.site.register(Availability)
admin.site.register(Booking)
admin.site.register(TimeOffRequest)
