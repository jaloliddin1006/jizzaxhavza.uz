from .views import index, CategoryView, CategoryDetailView
from django.urls import path



app_name = "app"
urlpatterns = [
    path("", index, name='index'),
    path("i/<int:id>", CategoryView.as_view(), name='post'),
    path("i/<int:category_id>/<int:id>", CategoryDetailView.as_view(), name='detail'),
]