# forms.py
from django import forms

from .models import ContactInterest


class ContactInterestForm(forms.ModelForm):
    class Meta:
        model = ContactInterest
        fields = ['name', 'email', 'phone_number', 'message']

