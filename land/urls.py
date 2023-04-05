"""land URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views 
from django.conf import settings #new
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index,name='home'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('services/',views.service,name='services'),
    path('blog-list/',views.blog_list,name='blog-list'),
    path('blog-sidebar/',views.blog_sidebar,name='blog-sidebar'),
    path('blog-details/',views.blog_details,name='blog-details'),
    path('blog-team/',views.blog_team,name='blog-team'),
    path('contact/',views.contact,name='contact')






]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

