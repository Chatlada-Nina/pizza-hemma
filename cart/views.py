from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """
    A view that render the cart contents page.
    """

    return render(request, 'cart/cart.html')