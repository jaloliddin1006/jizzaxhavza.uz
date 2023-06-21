from .views import index, CategoryView, CategoryDetailView, IndexView, UserDetailView
from django.urls import path



app_name = "app"
urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("i/<int:id>", CategoryView.as_view(), name='post'),
    path("i/<int:category_id>/<int:id>", CategoryDetailView.as_view(), name='detail'),
    path("user/<str:category_id>/<str:id>", UserDetailView.as_view(), name='user'),
    
]