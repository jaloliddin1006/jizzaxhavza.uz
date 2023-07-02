from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static, re_path
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
# from app.views import index

urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path('', include("app.urls")),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += i18n_patterns(
        path('', include("app.urls"))
)
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]