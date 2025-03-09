from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def contact_us(request):
    """
    Allow user contact requests.
    **Context**
    ``contact_form``
        An instance of :form: `contact.ContactForm`.
    **Template:**
    :template:`contact/contactus.html`
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Your request has been received. We aim to reply within 2 business days.")
    contact_form = ContactForm()

    return render(
        request,
        "contact/contactus.html",
        {"contact_form": contact_form},
    )
