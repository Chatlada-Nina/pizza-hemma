from django.shortcuts import render, redirect, reverse, HttpResponse

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
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if menu_id in list(cart.keys()):
        cart[menu_id] += quantity
    else:
        cart[menu_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, menu_id):
    """
    Update the quantity of the specified menu to the specified amount.
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[menu_id] = quantity
    else:
        cart.pop(menu_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))



def remove_from_cart(request, menu_id):
    """
    Remove the menu from the cart.
    """
    try:
        cart = request.session.get('cart', {})

        if menu_id in cart:
            cart.pop(menu_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=500)
