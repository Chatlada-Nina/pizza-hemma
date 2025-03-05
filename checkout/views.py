from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('menu'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QzJUzA9nJJdH1iNxK0UWCtrge1gNtI2BET9eipRwWFd4Azk8Ju3JoLIqeuaXEaEJx6Mb0PnpbpsroxPYCL144ik00MPuQBXeJ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)