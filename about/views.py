from django.shortcuts import render
from .models import About


def about_us(request):
    """
    Render the about page.
    Display an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The instance of :model:`about.About`.

    **Template**
    :template: `about/about.html`
    """
    about = About.objects.all().first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
