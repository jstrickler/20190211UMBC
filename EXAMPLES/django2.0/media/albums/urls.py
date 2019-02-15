"""
URL Configuration for albums
"""
from django.conf.urls import url
from .views import *   # import views from app

urlpatterns = [
    # add url patterns for the albums app here

    # Example:
#    url(r'^$', views.home, name='home'),
    url(r'^api/musicians/$', MusicianListView.as_view()),
    url(r'^api/musicians/(?P<pk>\d+)/$', MusicianView.as_view()),
    url(r'^api/albums/$', AlbumListView.as_view()),
    url(r'^api/albums/(?P<pk>\d+)/$', AlbumView.as_view()),
]
