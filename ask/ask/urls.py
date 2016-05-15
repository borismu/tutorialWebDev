"""ask URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from qa.views import test, test1

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', test1),
    url(r'^$', test1),
    url(r'^popular/', test1),
    url(r'^new/', test1),
    url(r'^ask/', test1),
    url(r'^login/', test1),
    # url(r'^question/', test),
    url(r'^question/(?P<id>\d+)/$', test),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(admin.site.urls)),
]
