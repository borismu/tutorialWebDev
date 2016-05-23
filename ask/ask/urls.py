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

from qa.views import test, test1, questions_popular, questions_new, question_detail, ask

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', test),
    # url(r'^$', test),
    url(r'^new/', test),
    url(r'^ask/', ask),
    url(r'^login/', test),
    url(r'^question/(?P<id>\d+)/$', question_detail
, name='question_detail'),
    url(r'^popular/', questions_popular, name='questions_popular'),
    url(r'^$', questions_new, name='questions_new'),
    # url(r'^question/', test),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(admin.site.urls)),
]
