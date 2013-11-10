from django.conf.urls import patterns, url

from serialWebPortal import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView, name='index'),
    url(r'^(?P<device_id>\d+)/$', views.DetailView, name='detail'),
    url(r'^(?P<device_id>\d+)/send_message$', views.SendMessageView, name='send_message'),
)
