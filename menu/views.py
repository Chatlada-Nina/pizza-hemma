from django.shortcuts import render
from .models import MenuItem, MenuList

# Create your views here.


def all_menus(request):
    """
    A view to show all menu, including sorting.
    """
    menus = MenuItem.objects.all()

    context = {
        'menus': menus,
    }

    return render(request, 'menu/menus.html', context)
