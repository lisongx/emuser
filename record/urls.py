from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # url(r'^$', 'emuser.views.home', name='home'),
    # url(r'^emuser/', include('emuser.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'record.views.courses'),
    url(r'^coursera/?$', 'record.views.coursera'),
)
