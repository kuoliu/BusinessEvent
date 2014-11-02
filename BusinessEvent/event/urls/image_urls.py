__author__ = 'lk'

from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^user/(?P<user_id>.+)$', 'event.small_views.photo.user_photo'),
    url(r'^news/(?P<news_id>.+)$', 'event.small_views.photo.news_photo'),
    url(r'^event/(?P<event_id>.+)$', 'event.small_views.photo.event_photo')
)