from django.test import TestCase
from django.urls import reverse
from .models import SubscribedUsers


class TestHomeViews(TestCase):
    """Tests for the home app views."""

    def test_home_page_loads_successfully(self):
        """Home page should load with a 200 status code."""
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_home_uses_correct_template(self):
        """Home page should use index.html template."""
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'home/index.html')

    def test_home_page_contains_expected_content(self):
        """Check if the home page contains a specific text."""
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, "Pizza Hemma")


class SubscribedUsersModelTest(TestCase):
    """ Tests for the subscription field"""
    def setUp(self):
        self.user = SubscribedUsers.objects.create(email="test@example.com")

    def test_create_subscribed_user(self):
        """Check a SubscribedUsers instance is created correctly"""
        user = SubscribedUsers.objects.get(email="test@example.com")
        self.assertEqual(user.email, "test@example.com")
        self.assertIsNotNone(user.created_on)

    def test_email_unique_constraint(self):
        """Check the email uniqueness"""
        with self.assertRaises(Exception):
            SubscribedUsers.objects.create(email="test@example.com")
