from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """
    A view that render the cart contents page.
    """

    return render(request, 'cart/cart.html')

def add_to_cart(request, menu_id):
    """
    Add a quantity of the specified menu to the cart.
    """
    quantity = int(request.GET.get('quantity'))
    redirect_url = request.GET.get('redirect_url')
    cart = request.session.get('cart', {})

    if menu_id in list(cart.keys()):
        cart[menu_id] += quantity
    else:
        cart[menu_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)