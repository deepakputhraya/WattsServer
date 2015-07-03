"""WattServer URL Configuration

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
from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from Team.views import teamMemberAPI
from Animal.views import animalAPI,adoptAPI,storyAPI

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/team/$', teamMemberAPI), #API TO ACCESS TEAM MEMBERS. Only GET request Works
    url(r'^api/animal/$', animalAPI), #API TO ACCESS All ANIMALS MEMBERS. Only GET request Works
    url(r'^api/adopt/$', adoptAPI), #API TO ACCESS ADOPTABLE ANIMALS MEMBERS. Only GET request Works
    url(r'^api/story/$', storyAPI), #API TO ACCESS "HAPPY TAILS" ANIMALS MEMBERS. Only GET request Works
)

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

admin.site.site_header = 'Watts Project Administrator'
