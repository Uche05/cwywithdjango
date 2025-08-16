from django.contrib.auth import views
from django.contrib.auth.views import LoginView
from django.urls import include, path

from . import views

urlpatterns = [
    
    path('', views.home, name='home'),                # Home page
    path('jobpost/', views.jobpost, name='jobpost'),   # Job post page
    path('contact/', views.contact, name='contact'),   # Contact page
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
    path('contact/', views.contact, name='contact'),
    path('recruitment/', views.recruitment, name='recruitment'),
    path('accounts/login/', LoginView.as_view(), name='login'),# Login page
    # Dashboards
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/staff/", views.staff_dashboard, name="staff_dashboard"),
    path("dashboard/client/", views.client_dashboard, name="client_dashboard"),
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path('logout/', views.logout_view, name='logout'),
    path('timeoff/add-json/', views.add_time_off_ajax, name='add_time_off_ajax'),
    path('availability/add_availability/', views.add_availability, name='add_availability'),      # POST JSON to add
    path('availability/view_availability/', views.view_availabilities, name='view_availabilities'),  # GET JSON list
    path('availability/delete_availability/<int:availability_id>/', views.delete_availability, name='delete_availability'),  # DELETE JSON
    path('admin/bookings/', views.admin_view_bookings, name='admin_view_bookings'),       # GET: view all bookings
    path('admin/bookings/add/', views.admin_add_booking, name='admin_add_booking'),       # POST: add new booking
    path('admin/bookings/edit/<int:booking_id>/', views.admin_edit_booking, name='admin_edit_booking'),  # POST/PUT: edit
    path('admin/bookings/delete/<int:booking_id>/', views.admin_delete_booking, name='admin_delete_booking'), # DELETE
    # Clients
    path('admin/clients/', views.admin_view_clients, name='admin_view_clients'),
    path('admin/clients/add/', views.admin_add_client, name='admin_add_client'),
    path('admin/clients/<int:client_id>/availabilities/', views.admin_view_client_availabilities, name='view_client_availabilities'),
    path('admin/clients/availabilities/add/', views.admin_add_client_availability, name='admin_add_client_availability'),
    # Staff
    path('admin/staff/', views.admin_view_staff, name='admin_view_staff'),
    path('admin/staff/add/', views.admin_add_staff, name='admin_add_staff'),
    # Bookings
    path('admin/bookings/', views.admin_view_bookings, name='admin_view_bookings'),
    path('admin/bookings/add/', views.admin_add_booking, name='admin_add_booking'),
    path('admin/bookings/<int:booking_id>/edit/', views.admin_edit_booking, name='edit_booking'),
    path('admin/bookings/<int:booking_id>/delete/', views.admin_delete_booking, name='delete_booking'),
    path('dashboard/admin/add_client/', views.add_client, name='add_client'),
    path('dashboard/admin/add_staff/', views.add_staff, name='add_staff'),
    path('dashboard/admin/add_booking/', views.add_booking, name='add_booking'),





]
