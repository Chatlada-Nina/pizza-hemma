from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import MenuItem, MenuList
from .forms import MenuForm

# Create your views here.


def all_menus(request):
    """
    A view to show all menu, including sorting.
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


def add_menu(request):
    """ Add a menu to the restaurant site """
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu added!")
            return redirect(reverse('add_menu'))
        else:
            messages.error(request, "Failed adding menu. Please ensure the form is valid.")
    else:
        form = MenuForm()

    template = 'menu/add_menu.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def update_menu(request, menu_id):
    """ Update a menu in the restaurant site """
    menu = get_object_or_404(MenuItem, pk=menu_id)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu updated!')
            return redirect(reverse('add_menu'))
        else:
            messages.error(request, 'Failed to update menu. Please ensure the form is valid.')
    else:
        form = MenuForm(instance=menu)
        messages.info(request, f'You are updating {menu.name}')

    template = 'menu/update_menu.html'
    context = {
        'form': form,
        'menu': menu,
    }

    return render(request, template, context)


def delete_menu(request, menu_id):
    """ Delete menu from the restaurant site """
    menu = get_object_or_404(MenuItem, pk=menu_id)
    menu.delete()
    messages.success(request, 'Menu deleted!')
    return redirect(reverse('all_menus'))