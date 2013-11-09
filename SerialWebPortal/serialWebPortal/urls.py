from django.conf.urls import patterns, url

from serialWebPortal import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<device_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<device_id>\d+)/send_message$', views.send_message, name='send_message'),
)
