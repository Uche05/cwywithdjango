from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import (Availability, Booking, ContactInterest, TimeOffRequest,
                     UserProfile)


# done with aid from ChatGPT
def home(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    user_type = profile.user_type

    context = {
        "user_type": user_type,
        "user": user,
    }

    if user_type == "Client":
        context["availabilities"] = Availability.objects.filter(customer=user)
        context["bookings"] = Booking.objects.filter(customer=user)

    elif user_type == "Staff":
        context["bookings"] = Booking.objects.filter(employee=user)
        context["time_off_requests"] = TimeOffRequest.objects.filter(employee=user)

    elif user_type == "Admin":
        context["all_bookings"] = Booking.objects.all()
        context["all_availabilities"] = Availability.objects.all()
        context["all_time_off_requests"] = TimeOffRequest.objects.all()

    return render(request, "blog/index.html", context)



from django.shortcuts import render


def jobpost(request):
    return render(request, 'blog/jobpost.html')  # Renders the job post page

def contact(request):
    return render(request, 'blog/contact.html')  # Renders the contact page

# Add any additional views here as needed
def privacy_policy(request):
    return render(request, 'blog/privacy_policy.html')  # Renders the privacy policy page

def terms_of_use(request):
    return render(request, 'blog/terms_of_use.html')  # Renders the terms of use page

def terms_and_conditions(request):
    return render(request, 'blog/terms_and_conditions.html')  # Renders the terms and conditions page

def recruitment(request):
    return render(request, 'blog/jobpost.html')  # Renders the recruitment page


from .forms import ContactInterestForm


def contact(request):
    # done with aid from ChatGPT
    # this view handles the contact form submission
    if request.method == 'POST':
        form = ContactInterestForm(request.POST)
        if form.is_valid():  # is_valid() is called on the form, not the model
            form.save()  # Save the valid form data to the database
            messages.success(request, 'Your interest has been registered successfully!')
            return redirect('contact')  # Redirect to the same contact page or another page
    else:
        form = ContactInterestForm()

    return render(request, 'blog/contact.html', {'form': form})
