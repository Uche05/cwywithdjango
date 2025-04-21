from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import redirect, render

from .forms import ContactInterestForm, JobApplicationForm
from .models import (Availability, Booking, ContactInterest, TimeOffRequest,
                     UserProfile)


# done with aid from ChatGPT
def home(request):
    context = {}

    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_type = user_profile.user_type
        context["user"] = user_profile
        context["user_type"] = user_type
        # (add more context here as needed)
    
    return render(request, "blog/index.html", context)



def jobpost(request):
    return render(request, "blog/jobpost.html")  # Renders the job post page


def contact(request):
    return render(request, "blog/contact.html")  # Renders the contact page


# Add any additional views here as needed
def privacy_policy(request):
    return render(
        request, "blog/privacy_policy.html"
    )  # Renders the privacy policy page


def terms_of_use(request):
    return render(request, "blog/terms_of_use.html")  # Renders the terms of use page


def terms_and_conditions(request):
    return render(
        request, "blog/terms_and_conditions.html"
    )  # Renders the terms and conditions page


def recruitment(request):
    form = None
    try:
        if request.method == "POST":
            form = JobApplicationForm(request.POST, request.FILES)
            if form.is_valid() and 'declaration' in request.POST:
                form.save()
                messages.success(request, "Your application has been submitted successfully!")
            else:
                form = JobApplicationForm()
                messages.error(request, "Please check the form for errors.")
        return render(request, "blog/recruitment.html", {"form": form})  # Renders the recruitment page
    except Exception as e:
        return HttpResponseServerError("An error occurred: " + str(e))

def contact(request):
    # done with aid from ChatGPT
    # this view handles the contact form submission
    if request.method == "POST":
        form = ContactInterestForm(request.POST)
        if form.is_valid():  # is_valid() is called on the form, not the model
            form.save()  # Save the valid form data to the database
            messages.success(request, "Your interest has been registered successfully!")
            return redirect(
                "contact"
            )  # Redirect to the same contact page or another page
    else:
        form = ContactInterestForm()

    return render(request, "blog/contact.html", {"form": form})


# dashbaords for registered users


@login_required
def staff_dashboard(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("Profile missing")

    if profile.user_type != "Staff":
        return HttpResponseForbidden("Access denied")

    bookings = Booking.objects.filter(employee=profile)
    time_off_requests = TimeOffRequest.objects.filter(employee=profile)

    return render(request, "dashboards/staff_dashboard.html", {
        "user": profile,
        "bookings": bookings,
        "time_off_requests": time_off_requests,
    })


# to make client and admin similar
@login_required
def client_dashboard(request):
    try:
        profile = request.user.userprofile
        if profile.user_type != "Client":
            return render(request, "403.html")
    except UserProfile.DoesNotExist:
        return render(request, "403.html")

    return render(request, "dashboards/client_dashboard.html")


@login_required
def admin_dashboard(request):
    try:
        profile = request.user.userprofile
        if profile.user_type != "Admin":
            return render(request, "403.html")
    except UserProfile.DoesNotExist:
        return render(request, "403.html")

    return render(request, "dashboards/admin_dashboard.html")
