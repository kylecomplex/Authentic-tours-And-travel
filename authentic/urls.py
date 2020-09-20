from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tour.urls')),
    path('account/', include('account.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()