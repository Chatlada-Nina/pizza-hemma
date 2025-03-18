from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import SubscribedUsers

# Create your views here.


def homepage(request):
    """
    A view to return the index page.
    """
    return render(request, 'home/index.html')


def subscribe(request):
    """
    A view for subscribe section
    """
    if request.method == 'POST':
        email = request.POST.get('email', None)

        # Validate email first
        if not email:
            messages.error(request, 'You must type a valid email to subscribe.')
            return redirect("/")

        try:
            validate_email(email)  # Validate format before querying the database
        except ValidationError:
            messages.error(request, 'Invalid email address. Please enter a valid one.')
            return redirect("/")
        
        user = request.user  # Get logged-in user

        # Allow registered users to subscribe
        if user.is_authenticated and user.email == email:
            subscribed_user, created = SubscribedUsers.objects.get_or_create(email=email)
            if created:
                messages.success(request, f'{email} was successfully subscribed!')
            else:
                messages.info(request, f'{email} is already subscribed!')
            return redirect("/")
        
        # Check if the email belongs to a registered user (not logged in)
        if get_user_model().objects.filter(email=email).exists():
            messages.error(request, f'Found registered user with associated email {email}. You must log in to subscribe.')
            return redirect("/")

        # Check if already subscribed
        if SubscribedUsers.objects.filter(email=email).exists():
            messages.error(request, f'{email} is already subscribed!')
            return redirect("/")

        # Save to the subscription model
        SubscribedUsers.objects.create(email=email)
        messages.success(request, f'{email} was successfully subscribed!')
        return redirect("/")

    return redirect("/")