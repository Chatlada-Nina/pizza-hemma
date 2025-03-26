from django.test import TestCase
from django.urls import reverse
from .models import About


# ----------- VIEWS TESTING ------------
class TestAboutViews(TestCase):
    """Test the about views"""

    def setUp(self):
        """Set up About instance"""
        self.about = About.objects.create(
            title="About us",
            content="Welcome to Pizza Hemma"
        )

    def test_about_page_loads_successfully(self):
        """About page Should load with a 200 status code."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_uses_correct_template(self):
        """About page Should use about.html template."""
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about/about.html')

    def test_about_page_contains_expected_content(self):
        """Check the about page contains the expected content."""
        response = self.client.get(reverse('about'))
        self.assertContains(response, "Welcome to Pizza Hemma")

    def test_about_page_context_data(self):
        """Check the about page context contains the About instance."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.context['about'], self.about)


# ----------- MODELS TESTING ------------
class TestAboutModel(TestCase):
    """Test the About model."""

    def setUp(self):
        """Set up About Instance"""
        self.about = About.objects.create(
            title="About us",
            content="Welcome to Pizza Hemma"
        )

    def test_about_model_creation(self):
        """Check an About instance is created correctly."""
        about = About.objects.get(title="About us")
        self.assertEqual(about.content, "Welcome to Pizza Hemma")

    def test_about_model_str_method(self):
        """Test the __str__ method of the About model."""
        self.assertEqual(str(self.about), "About us")
