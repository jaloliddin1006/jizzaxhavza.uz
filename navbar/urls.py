from .views import sidebar_and_navbar_items
from django.urls import path
urlpatterns = [
    path('', sidebar_and_navbar_items, name='index')
]