from django.shortcuts import render
from navbar.models import NavbarCategory
# Create your views here.
def index(request):
    navbar = NavbarCategory.objects.filter(status='navbar')
    navbar = [i for i in navbar]
    print(navbar)
    return render(request, 'index.html', context={'navbar': navbar})