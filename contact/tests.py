from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from contact.models import Contact


# ----------- MODELS TESTING ------------
class TestContactModel(TestCase):
    """ Test the Contact model. """

    def setUp(self):
        """Set up a test contact instance."""
        self.contact = Contact.objects.create(
            name="Fiona Carters",
            email="fionacart@example.com",
            message="This is a test contact message."
        )

    def test_contact_creation(self):
        """Check a Contact instance is created correctly."""
        contact = Contact.objects.get(email="fionacart@example.com")
        self.assertEqual(contact.name, "Fiona Carters")
        self.assertEqual(contact.email, "fionacart@example.com")
        self.assertEqual(contact.message, "This is a test contact message.")
        self.assertFalse(contact.read)

    def test_contact_str_method(self):
        """Check the __str__ method returns the expected string."""
        self.assertEqual(str(self.contact), "Contact from Fiona Carters")

    def test_mark_contact_as_read(self):
        """Check updating the 'read' field of a Contact instance."""
        self.contact.read = True
        self.contact.save()
        updated_contact = Contact.objects.get(email="fionacart@example.com")
        self.assertTrue(updated_contact.read)


# ----------- VIEWS TESTING ------------
class TestContactViews(TestCase):
    """ Test the Contact views. """

    def setUp(self):
        """Set up the test client and data."""
        self.client = Client()
        self.contact_url = reverse('contact')
        self.user = User.objects.create_user(
            username='fiona01',
            password='123456789',
            first_name='Fiona',
            last_name='Carters',
            email='fionacart@example.com'
        )

    def test_contact_page_loads_successfully(self):
        """Check if the contact page loads with a 200 status code."""
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contactus.html')

    def test_contact_form_submission(self):
        """Test submitting the contact form successfully."""
        response = self.client.post(self.contact_url, {
            'name': 'Lara Carters',
            'email': 'laracart@example.com',
            'message': 'This is a second contact test message.'
        })

        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, 'Lara Carters')
        self.assertEqual(contact.email, 'laracart@example.com')
        self.assertEqual(
            contact.message, 'This is a second contact test message.')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Your request has been received."
            " We aim to reply within 2 business days."
        )

    def test_missing_name_field(self):
        """Check the form is invalid if the name field is missing."""
        response = self.client.post(self.contact_url, {
            'email': 'test@example.com',
            'message': 'This is a test message without a name.'
        })
        self.assertFormError(
            response, 'contact_form', 'name', 'This field is required.')

    def test_missing_email_field(self):
        """Check the form is invalid if the email field is missing."""
        response = self.client.post(self.contact_url, {
            'name': 'Test',
            'message': 'This is a test message without an email.'
        })
        self.assertFormError(
            response, 'contact_form', 'email', 'This field is required.')

    def test_invalid_email_format(self):
        """Check the form is invalid if the email format is incorrect."""
        response = self.client.post(self.contact_url, {
            'name': 'Test',
            'email': 'dethhfgde',
            'message': 'This is a test message with an invalid email format.'
        })
        self.assertFormError(
            response, 'contact_form', 'email', 'Enter a valid email address.')

    def test_empty_message_field(self):
        """Check the form is invalid if the message field is empty."""
        response = self.client.post(self.contact_url, {
            'name': 'Test',
            'email': 'test@example.com',
            'message': ''
        })
        self.assertFormError(
            response, 'contact_form', 'message', 'This field is required.')
