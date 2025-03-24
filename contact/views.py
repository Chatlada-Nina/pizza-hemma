from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def contact_us(request):
    """
    Allow user contact requests.

    **Context**
    ``contact_form``
        A form for users to submit contact requests.

    **Template:**
    :template:`contact/contactus.html`
    """
    if request.method == "POST":
        if request.user.is_authenticated:
            contact_form = ContactForm(data=request.POST, initial={
                'name': request.user.get_full_name(),
                'email': request.user.email,
            })
        else:
            contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            if request.user.is_authenticated:
                contact.name = request.user.get_full_name()
                contact.email = request.user.email
            contact.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "Your request has been received. "
                "We aim to reply within 2 business days."
            )
            contact_form = ContactForm()

    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.get_full_name(),
                'email': request.user.email,
            }
        contact_form = ContactForm(initial=initial_data)

    return render(
        request,
        "contact/contactus.html",
        {"contact_form": contact_form},
    )
