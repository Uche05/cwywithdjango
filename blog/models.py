# User Model
from django.contrib.auth.models import User
# Create your models here.
from django.db import models


class UserProfile(models.Model):
    USER_TYPES = [
        ('Staff', 'Staff'),
        ('Client', 'Client'),
        ('Admin', 'Admin'),
    ]

    # Reference to Django's default User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='Client')
    location = models.CharField(max_length=255, blank=True, null=True)  # Only for Clients
    
    def __str__(self):
        return f"{self.user.username} ({self.user_type})"


# Availability (Set by Clients)
class Availability(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'Client'}) #fk to Client user
    #note that this means that there will be many availabilities to one customer
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return f"Availability {self.id} ({self.status})"

# Bookings (Employees Assigned to Client Availability)
class Booking(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_bookings', limit_choices_to={'user_type': 'Client'}) #fk to Client user
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_bookings', limit_choices_to={'user_type': 'Staff'}) #fk to Staff user
    availability = models.ForeignKey(Availability, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')

    class Meta:
        ordering = ['-booking_date']
    
    def __str__(self):
        return f"Booking {self.id} ({self.status})"

# Employee Absence Report (Time Off Requests)
class TimeOffRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('DENIED', 'Denied'),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'Staff'})
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"TimeOffRequest {self.id} ({self.status})"

