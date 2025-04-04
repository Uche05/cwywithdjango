from django.urls import path

from . import views

urlpatterns = [
    path('', views.AvailabilityListView.as_view(), name='home'),
]