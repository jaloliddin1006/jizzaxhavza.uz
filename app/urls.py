from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index')
]