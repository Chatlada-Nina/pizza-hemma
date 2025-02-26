from django.shortcuts import render
from .models import MenuItem, MenuList

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
