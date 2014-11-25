from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BusinessEvent.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^news/', 'event.views.home'),
    url(r'^event/', include('event.urls.urls')),

    url(r'^image/', include('event.urls.image_urls')),
    url(r'^my_events/$', 'event.views.my_events'),
    url(r'^my_friends/', 'event.views.my_friends'),
    url(r'^user/(?P<user_id>.+)$', 'event.small_views.link.user_page'),

    url(r'^publish/$', 'event.small_views.link.publish_news'),
    url(r'^publish/publish_news$', 'event.views.publish'),
    url(r'^new_event/$', 'event.small_views.link.publish_event'),
    url(r'^new_event/publish_event$', 'event.views.new_event'),
    url(r'^contact/', 'event.views.contact'),
    url(r'^all_user/$', 'event.views.all_user'),
    url(r'^all_events/$', 'event.views.all_event'),
)
