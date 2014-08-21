from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'uploads.views.list', name='list'),
    url(r'^upload/', include('uploads.urls', namespace="uploads")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)