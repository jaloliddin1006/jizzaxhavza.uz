from .views import index, article, CategoryView
from django.urls import path



app_name = "app"
urlpatterns = [
    path("", index, name='index'),
    path("i/<int:id>", CategoryView.as_view(), name='post'),
]