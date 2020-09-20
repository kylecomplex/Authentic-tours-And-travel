from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .import views

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('services/', services_view, name='services'),
    path('send_message/', send_message, name='send_message'),
    path('packages/', packages_view, name='packages'),
    path('booking/', booking_view, name='booking'),
    path('articles/', views.ArticleList.as_view(), name='article_list'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    #additional
    
]
urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
