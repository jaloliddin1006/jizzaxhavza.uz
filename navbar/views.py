from django.shortcuts import render
from .models import NavbarCategory
# Create your views here.

from django import template



# def index(request):
#     navbar_categories = NavbarCategory.objects.filter(status='navbar')
#     sidebar_categories = NavbarCategory.objects.filter(status='sidebar')

#     context = {
#         'navbar_categories': navbar_categories,
#         'sidebar_categories': sidebar_categories,
#     }

#     return render(request, 'index.html')

def all_page_categories(request):
    navbar_categories = NavbarCategory.objects.filter(status='navbar')
    sidebar_categories = NavbarCategory.objects.filter(status='sidebar')

    context = {
        'navbar_categories': navbar_categories,
        'sidebar_categories': sidebar_categories,
    }

    return context

