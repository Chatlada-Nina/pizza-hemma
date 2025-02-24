from django.shortcuts import render
from .models import About

# Create your views here.


def about_us(request):
    """
    Render the about page
    """
    about = About.objects.all().first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
