import json

from django import forms
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import (HttpResponseForbidden, HttpResponseServerError,
                        JsonResponse)
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

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
    availabilities = Availability.objects.filter(customer=profile.user)  # read-only

    return render(request, "dashboards/staff_dashboard.html", {
        "user": profile,
        "bookings": bookings,
        "time_off_requests": time_off_requests,
        "availabilities": availabilities,
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
    availabilities = Availability.objects.filter(customer=profile.user)

    return render(request, "dashboards/client_dashboard.html", {
        "user": profile,
        "bookings": bookings,
        "availabilities": availabilities,
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

#CRUD for availabilities
# Dynamic CRUD

@csrf_exempt  # allow AJAX POST requests
def add_time_off_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_request = TimeOffRequest.objects.create(
            employee=request.user,
            start_date=data['start_date'],
            end_date=data['end_date'],
            reason=data['reason'],
            status='Pending'
        )
        return JsonResponse({
            "id": new_request.id,
            "start_date": new_request.start_date,
            "end_date": new_request.end_date,
            "reason": new_request.reason,
            "status": new_request.status
        })

# View all availabilities for the logged-in client
def view_availabilities(request):
    if request.method == "GET":
        availabilities = Availability.objects.filter(customer=request.user)
        data = [
            {
                "id": a.id,
                "start_date": a.start_date,
                "end_date": a.end_date,
                "status": a.status
            } for a in availabilities
        ]
        return JsonResponse({"availabilities": data})
    return JsonResponse({"error": "Invalid request method"}, status=405)

# Add new availability
@csrf_exempt
def add_availability(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            start_date = data.get("start_date")
            end_date = data.get("end_date")
            status = data.get("status", "OPEN")  # default to OPEN

            new_availability = Availability.objects.create(
                customer=request.user,
                start_date=start_date,
                end_date=end_date,
                status=status
            )

            return JsonResponse({
                "id": new_availability.id,
                "start_date": new_availability.start_date,
                "end_date": new_availability.end_date,
                "status": new_availability.status
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

# Delete availability
@csrf_exempt
def delete_availability(request, availability_id):
    if request.method == "DELETE":
        try:
            availability = Availability.objects.get(id=availability_id, customer=request.user)
            availability.delete()
            return JsonResponse({"success": True})
        except Availability.DoesNotExist:
            return JsonResponse({"error": "Availability not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
