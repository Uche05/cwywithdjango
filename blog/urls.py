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


]
