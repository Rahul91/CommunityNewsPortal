"""NewsPortal URL Configuration

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
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'News.views.home'),
    #url(r'^index/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'News.views.login'),
    url(r'^accounts/auth/$', 'News.views.auth_view'),
    url(r'^$','News.views.home'),
    url(r'^accounts/logout/$', 'News.views.logout'),
    url(r'^accounts/loggedin/(?P<id>\d+)/$', 'News.views.loggedin'),
    url(r'^accounts/invalid/$', 'News.views.invalid_login'),
    url(r'^accounts/register/$', 'News.views.register_user'),
    url(r'^accounts/register_success/$', 'News.views.register_success'),
    url(r'^accounts/bad_request/$', 'News.views.bad_request'),
    #url(r'^news/add_news/$', 'News.views.add_news'),
    url(r'^news/get/(?P<id>\d+)/$', 'News.views.news_single'),
    url(r'^upvotes/(?P<id>\d+)/$', 'News.views.upvotes'),
    url(r'^news/add_news/user/(?P<id>\d+)/$', 'News.views.add_news'),
]
