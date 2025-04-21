# forms.py
from django import forms

from .models import ContactInterest, JobApplication


class ContactInterestForm(forms.ModelForm):
    class Meta:
        model = ContactInterest
        fields = ['name', 'email', 'phone_number', 'message']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'number', 'email', 'start_date' ,'file']
