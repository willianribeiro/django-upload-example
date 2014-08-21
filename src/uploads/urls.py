from django.conf.urls import patterns, url

urlpatterns = patterns('uploads.views',
    url(r'^$', 'list', name='list'),
    url(r'^list', 'list', name='list')
)