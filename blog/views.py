from django import forms
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactInterestForm, JobApplicationForm
from .models import (Availability, Booking, ContactInterest, TimeOffRequest,
                     UserProfile)


#   Home page
def home(request):
    context = {}

    if request.user.is_authenticated:
        # Get or create UserProfile automatically
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        context["user"] = profile
        context["user_type"] = profile.user_type

    return render(request, "blog/index.html", context)


def jobpost(request):
    return render(request, "blog/jobpost.html")


def contact(request):
    if request.method == "POST":
        form = ContactInterestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your interest has been registered successfully!")
            return redirect("contact")
        else:
            messages.error(request, "Please check the form for errors.")
    else:
        form = ContactInterestForm()

    return render(request, "blog/contact.html", {"form": form})


def privacy_policy(request):
    return render(request, "blog/privacy_policy.html")


def terms_of_use(request):
    return render(request, "blog/terms_of_use.html")


def terms_and_conditions(request):
    return render(request, "blog/terms_and_conditions.html")


def recruitment(request):
    form = None
    try:
        if request.method == "POST":
            form = JobApplicationForm(request.POST, request.FILES)
            if form.is_valid() and 'declaration' in request.POST:
                form.save()
                messages.success(request, "Your application has been submitted successfully!")
                return redirect("recruitment")
            else:
                messages.error(request, "Please check the form for errors.")
        else:
            form = JobApplicationForm()

        return render(request, "blog/recruitment.html", {"form": form})
    except Exception as e:
        return HttpResponseServerError("An error occurred: " + str(e))

# Dashboards

@login_required
def staff_dashboard(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("Profile missing")

    if profile.user_type != "Staff":
        return HttpResponseForbidden("Access denied")

    bookings = Booking.objects.filter(employee=profile.user)
    time_off_requests = TimeOffRequest.objects.filter(employee=profile.user)

    return render(request, "dashboards/staff_dashboard.html", {
        "user": profile,
        "bookings": bookings,
        "time_off_requests": time_off_requests,
    })



@login_required
def client_dashboard(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("Profile missing")

    if profile.user_type != "Client":
        return HttpResponseForbidden("Access denied")

    bookings = Booking.objects.filter(customer=profile.user)
    time_off_requests = TimeOffRequest.objects.filter(employee=profile.user)

    return render(request, "dashboards/client_dashboard.html", {
        "user": profile,
        "bookings": bookings,
        "time_off_requests": time_off_requests,
    })



@login_required
def admin_dashboard(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("Profile missing")

    if profile.user_type != "Admin":
        return HttpResponseForbidden("Access denied")

    return render(request, "dashboards/admin_dashboard.html", {"user": profile})

#log out view
def logout_view(request):
    logout(request)
    return redirect('login')

#CRUD Capabilites
@login_required
def add_availability(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        status = request.POST.get('status')

        Availability.objects.create(
            customer=request.user,
            start_date=start_date,
            end_date=end_date,
            status=status
        )
        return redirect('client_dashboard')

    return render(request, 'add_availability.html')


@login_required
def edit_availability(request, pk):
    availability = get_object_or_404(Availability, pk=pk, customer=request.user)

    if request.method == 'POST':
        availability.start_date = request.POST.get('start_date')
        availability.end_date = request.POST.get('end_date')
        availability.status = request.POST.get('status')
        availability.save()
        return redirect('client_dashboard')

    return render(request, 'edit_availability.html', {'availability': availability})


@login_required
def delete_availability(request, pk):
    availability = get_object_or_404(Availability, pk=pk, customer=request.user)
    if request.method == 'POST':
        availability.delete()
        return redirect('client_dashboard')