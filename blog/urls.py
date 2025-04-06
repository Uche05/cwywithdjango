from django.contrib.auth import views
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home, name='home'),                # Home page
    path('jobpost/', views.jobpost, name='jobpost'),   # Job post page
    path('contact/', views.contact, name='contact'),   # Contact page
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
    # urls.py
    path('contact/', views.contact, name='contact'),
    path('recruitment/', views.recruitment, name='jobpost'),
    path('accounts/login/', LoginView.as_view(), name='login'), # Login page
]
