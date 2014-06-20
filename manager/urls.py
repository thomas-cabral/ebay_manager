__author__ = 'Thomas'
from django.conf.urls import patterns, url
from manager import views


urlpatterns = patterns('',
    url(r'^$', views.AngularIndex.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),

    url(r'^angular_index/$', views.AngularMain.as_view()),
    url(r'^angular_detail/$', views.AngularDetail.as_view()),
    url(r'^angular_new/$', views.AngularNew.as_view()),

    url(r'^api/items/$', views.ItemApiList.as_view()),
    url(r'^api/item/(?P<pk>[0-9]+)/$', views.ItemApiDetail.as_view()),
)