"""themesedx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from admintheme.views import staffdashboard, admindashboard
from django.contrib.auth.decorators import permission_required


urlpatterns = [
    url(r'^dashboard/$', permission_required('is_superuser')(admindashboard)),
    url(r'^dashboard/$', permission_required('is_staff')(staffdashboard)),
    url(r'^user/', include('registration.urls')),

    url(r'^instances/add/', 'admintheme.views.add_instance'),

    url(r'^users/$', 'admintheme.views.users'),
    url(r'^users/add', 'admintheme.views.add_user'),


]
