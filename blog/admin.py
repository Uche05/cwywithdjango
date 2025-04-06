from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import (Availability, Booking, ContactInterest, TimeOffRequest,
                     UserProfile)


@admin.register(Availability)
class AvailabilityAdmin(SummernoteModelAdmin):
    list_display = ('customer', 'start_date', 'end_date', 'status')
    search_fields = ('status',)
    list_filter = ('status',)
    summernote_fields = ('description',)  # Make sure this field exists in your model

@admin.register(ContactInterest)
class ContactInterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')

    

# Register your models here.
admin.site.register(UserProfile)
# admin.site.register(Availability)
admin.site.register(Booking)
admin.site.register(TimeOffRequest)
