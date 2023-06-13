from django.shortcuts import render
from .models import NavbarCategory
# Create your views here.


def sidebar_and_navbar_items(request):
    navbar_categories = NavbarCategory.objects.filter(status='navbar')
    sidebar_categories = NavbarCategory.objects.filter(status='sidebar')

    context = {
        'navbar_categories': navbar_categories,
        'sidebar_categories': sidebar_categories,
    }

    return render(request, 'index.html', context)