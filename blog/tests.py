import os
import unittest

import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cwyproject.settings')

# Initialize Django
django.setup()

# Now import Django models and TestCase
from django.contrib.auth.models import User
from django.test import TestCase


class AdminDashboardTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_exists(self):
        # Test that the user was created successfully
        user_count = User.objects.filter(username='testuser').count()
        self.assertEqual(user_count, 1)

    def test_dummy_example(self):
        # Example placeholder test
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
