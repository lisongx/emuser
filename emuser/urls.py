from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    # url(r'^$', 'emuser.views.home', name='home'),
    # url(r'^emuser/', include('emuser.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resume/(?P<user_id>\d+)/$', 'record.views.resume'),
    url(r'^/?$', 'record.views.index'),
)
