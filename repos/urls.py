from django.conf.urls import patterns, url

from repos import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/files/$', views.FilesView.as_view(), name='files'),
    url(r'^(?P<file_id>\d+)/delete/$', views.delete, name='delete'),
)