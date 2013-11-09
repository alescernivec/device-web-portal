from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^devices/', include('serialWebPortal.urls', namespace="devices")),
    url(r'^admin/', include(admin.site.urls)),
)
