import json

from django import forms
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

# view all bookings
def admin_view_bookings(request):
    if request.method == 'GET':
        bookings = Booking.objects.all().order_by('-booking_date')
        data = []
        for b in bookings:
            data.append({
                'id': b.id,
                'customer': b.customer.username,
                'employee': b.employee.username,
                'availability_id': b.availability.id,
                'start': b.availability.start_date,
                'end': b.availability.end_date,
                'status': b.status,
            })
        return JsonResponse({'bookings': data})


# add new booking
@csrf_exempt
def admin_add_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer = get_object_or_404(User, id=data.get('customer_id'))
        employee = get_object_or_404(User, id=data.get('employee_id'))
        availability = get_object_or_404(Availability, id=data.get('availability_id'))
        status = data.get('status', 'OPEN')

        booking = Booking.objects.create(
            customer=customer,
            employee=employee,
            availability=availability,
            status=status
        )
        return JsonResponse({'success': True, 'booking_id': booking.id})


#edit booking
@csrf_exempt
def admin_edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method in ['POST', 'PUT']:
        data = json.loads(request.body)
        if 'status' in data:
            booking.status = data['status']
        if 'employee_id' in data:
            booking.employee = get_object_or_404(User, id=data['employee_id'])
        booking.save()
        return JsonResponse({'success': True, 'booking_id': booking.id})


# delete booking
@csrf_exempt
def admin_delete_booking(request, booking_id):
    if request.method == 'DELETE' or request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return JsonResponse({'success': True})

#ADMIN VIEWS
def admin_view_clients(request):
    if request.user.userprofile.user_type != 'Admin':
        return JsonResponse({'success': False, 'message': 'Unauthorized'}, status=403)

    clients = UserProfile.objects.filter(user_type='Client')
    client_list = [
        {
            'id': c.user.id,
            'first_name': c.user.first_name,
            'last_name': c.user.last_name,
            'email': c.user.email,
            'location': c.location
        } for c in clients
    ]
    return JsonResponse({'success': True, 'clients': client_list})

@csrf_exempt
def admin_add_client(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        location = request.POST.get("location", "")
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email already exists.'})
        
        user = User.objects.create(username=email, first_name=first_name, last_name=last_name, email=email)
        UserProfile.objects.create(user=user, user_type='Client', location=location)
        return JsonResponse({'success': True, 'message': 'Client added successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# Admin staff views
def admin_view_staff(request):
    if request.user.userprofile.user_type != 'Admin':
        return JsonResponse({'success': False, 'message': 'Unauthorized'}, status=403)

    staff_members = UserProfile.objects.filter(user_type='Staff')
    staff_list = [
        {
            'id': s.user.id,
            'first_name': s.user.first_name,
            'last_name': s.user.last_name,
            'email': s.user.email,
        } for s in staff_members
    ]
    return JsonResponse({'success': True, 'staff': staff_list})

@csrf_exempt
def admin_add_staff(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email already exists.'})
        
        user = User.objects.create(username=email, first_name=first_name, last_name=last_name, email=email)
        UserProfile.objects.create(user=user, user_type='Staff')
        return JsonResponse({'success': True, 'message': 'Staff added successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# admin client views
def admin_view_client_availabilities(request, client_id):
    client = get_object_or_404(User, id=client_id)
    availabilities = Availability.objects.filter(customer=client)
    data = [
        {'id': a.id, 'start_date': a.start_date, 'end_date': a.end_date, 'status': a.status}
        for a in availabilities
    ]
    return JsonResponse({'success': True, 'availabilities': data})

@csrf_exempt
def admin_add_client_availability(request):
    if request.method == "POST":
        client_id = request.POST.get("client_id")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        status = request.POST.get("status", "OPEN")
        
        client = get_object_or_404(User, id=client_id)
        Availability.objects.create(customer=client, start_date=start_date, end_date=end_date, status=status)
        return JsonResponse({'success': True, 'message': 'Availability added successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# admin booking views
def admin_view_bookings(request):
    bookings = Booking.objects.all()
    data = [
        {
            'id': b.id,
            'customer': f"{b.customer.first_name} {b.customer.last_name}",
            'employee': f"{b.employee.first_name} {b.employee.last_name}",
            'availability': f"{b.availability.start_date} - {b.availability.end_date}",
            'status': b.status,
        } for b in bookings
    ]
    return JsonResponse({'success': True, 'bookings': data})

@csrf_exempt
def admin_add_booking(request):
    if request.method == "POST":
        client_id = request.POST.get("client")
        staff_id = request.POST.get("staff")
        availability_id = request.POST.get("availability")
        status = request.POST.get("status", "OPEN")
        
        client = get_object_or_404(User, id=client_id)
        staff = get_object_or_404(User, id=staff_id)
        availability = get_object_or_404(Availability, id=availability_id)
        
        Booking.objects.create(customer=client, employee=staff, availability=availability, status=status)
        return JsonResponse({'success': True, 'message': 'Booking added successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@csrf_exempt
def admin_edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        booking.status = request.POST.get("status", booking.status)
        booking.save()
        return JsonResponse({'success': True, 'message': 'Booking updated successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@csrf_exempt
def admin_delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        booking.delete()
        return JsonResponse({'success': True, 'message': 'Booking deleted successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@csrf_exempt
def add_client(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        location = request.POST.get("location", "")

        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "message": "User with this email already exists."})

        user = User.objects.create(username=email, first_name=first_name, last_name=last_name, email=email)
        UserProfile.objects.create(user=user, user_type='Client', location=location)
        return JsonResponse({"success": True, "message": "Client added successfully."})

    return JsonResponse({"success": False, "message": "Invalid request."})

@csrf_exempt
def add_staff(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "message": "User with this email already exists."})

        user = User.objects.create(username=email, first_name=first_name, last_name=last_name, email=email)
        UserProfile.objects.create(user=user, user_type='Staff')
        return JsonResponse({"success": True, "message": "Staff added successfully."})

    return JsonResponse({"success": False, "message": "Invalid request."})

@csrf_exempt
def add_booking(request):
    if request.method == "POST":
        client_id = request.POST.get("client")
        staff_id = request.POST.get("staff")
        availability_id = request.POST.get("availability")
        status = request.POST.get("status")

        try:
            client = User.objects.get(id=client_id)
            staff = User.objects.get(id=staff_id)
            availability = Availability.objects.get(id=availability_id)
            Booking.objects.create(customer=client, employee=staff, availability=availability, status=status)
            return JsonResponse({"success": True, "message": "Booking added successfully."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    return JsonResponse({"success": False, "message": "Invalid request."})


