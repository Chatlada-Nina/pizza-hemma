from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import MenuItem, MenuList
from .forms import MenuForm


def all_menus(request):
    """
    Display all menu items, with optional filtering by menu list.

    If a 'menu_list' parameter is present in the request, filters the menu
    items to only include those belonging to the specified menu list(s).

    Args:
        request (HttpRequest): The HTTP request object containing GET
        parameters.

    Returns:
        HttpResponse: The rendered menu page with filtered or unfiltered menu
        items.
    """
    menus = MenuItem.objects.all()
    menu_lists = []

    if request.GET:
        if 'menu_list' in request.GET:
            menu_lists = request.GET['menu_list'].split(',')
            menus = menus.filter(menu_list__name__in=menu_lists)
            menu_lists = MenuList.objects.filter(name__in=menu_lists)

    context = {
        'menus': menus,
        'current_menu_lists': menu_lists,
    }

    return render(request, 'menu/menus.html', context)


@login_required
def add_menu(request):
    """
    Allow admin users to add a new menu item to the restaurant.

    Only superusers can access this view. Handles both GET (form display)
    and POST (form submission) requests.

    Args:
        request (HttpRequest): The HTTP request object containing form data.

    Returns:
        HttpResponse: Redirects to the add menu page on success, or re-renders
        the form with errors on failure.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that')
        return redirect(reverse('homepage'))

    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu added!")
            return redirect(reverse('add_menu'))
        else:
            messages.error(
                request, "Failed adding menu."
                "Please ensure the form is valid."
                )
    else:
        form = MenuForm()

    template = 'menu/add_menu.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_menu(request, menu_id):
    """
    Allow admin users to update an existing menu item.

    Only superusers can access this view. Handles both GET (form display)
    and POST (form submission) requests.

    Args:
        request (HttpRequest): The HTTP request object containing form data.
        menu_id (int): The ID of the menu item to be updated.

    Returns:
        HttpResponse: Redirects to the add menu page on success, or re-renders
        the form with errors on failure.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that')
        return redirect(reverse('homepage'))
    menu = get_object_or_404(MenuItem, pk=menu_id)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu updated!')
            return redirect(reverse('add_menu'))
        else:
            messages.error(
                request, 'Failed to update menu.'
                'Please ensure the form is valid.'
                )
    else:
        form = MenuForm(instance=menu)
        messages.info(request, f'You are updating {menu.name}')

    template = 'menu/update_menu.html'
    context = {
        'form': form,
        'menu': menu,
    }

    return render(request, template, context)


@login_required
def delete_menu(request, menu_id):
    """
    Allow admin users to delete a menu item from the restaurant.
    Only superusers can access this view.

    Args:
        request (HttpRequest): The HTTP request object.
        menu_id (int): The ID of the menu item to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the all menus page after deletion.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that')
        return redirect(reverse('homepage'))
    menu = get_object_or_404(MenuItem, pk=menu_id)
    menu.delete()
    messages.success(request, 'Menu deleted!')
    return redirect(reverse('all_menus'))
