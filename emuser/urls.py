from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', 'record.views.index'),
    url(r'^courses/', include('record.urls')),
    url(r'^resume/$', 'record.views.resume_index'),
    url(r'^resume/views/resume.html$', 'record.views.resume_resume'),
    url(r'^resume/(?P<user_id>\d+)/$', 'record.views.resume'),
    url(r'^user/$', 'record.views.fake_user'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
)
