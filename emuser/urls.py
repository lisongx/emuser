from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', 'record.views.index'),
    url(r'^courses/', include('record.urls')),
    url(r'^resume/(?P<user_id>\d+)/$', 'record.views.resume'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
)
