from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_cart(request):
    """
    Display the shopping cart page.

    This view retrieves the current cart data from the session and renders
    the cart template, allowing users to review their selected items before
    checkout.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered cart page.
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, menu_id):
    """
    Add a specified quantity of a menu item to the shopping cart.

    This function retrieves the quantity from the POST request and updates
    the cart stored in the session. If the item already exists in the cart,
    its quantity is incremented. Otherwise, it is added as a new entry.

    Args:
        request (HttpRequest): The HTTP request object containing form data.
        menu_id (int): The ID of the menu item being added.

    Returns:
        HttpResponseRedirect: Redirects the user back to the specified URL
        after adding the item to the cart.
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
    Update the quantity of a specific menu item in the shopping cart.

    This function retrieves the updated quantity from the POST request and
    modifies the cart stored in the session. If the quantity is greater than
    zero, the item's quantity is updated. If the quantity is zero or less,
    the item is removed from the cart.

    Args:
        request (HttpRequest): The HTTP request object containing form data.
        menu_id (int): The ID of the menu item to be updated.

    Returns:
        HttpResponseRedirect: Redirects the user back to the cart page after
        updating the item.
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
    Remove a specific menu item from the shopping cart.

    This function retrieves the cart from the session and removes the specified
    menu item if it exists. If the operation is successful, it returns HTTP 200
    status. If an exception occurs, it returns HTTP 500 status.

    Args:
        request (HttpRequest): The HTTP request object containing session data.
        menu_id (int): The ID of the menu item to be removed.

    Returns:
        HttpResponse: An HTTP response with status 200 if successful, or 500 if
        an error occurs.
    """
    try:
        cart = request.session.get('cart', {})

        if menu_id in cart:
            cart.pop(menu_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
