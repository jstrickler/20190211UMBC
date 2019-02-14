"""
URL Configuration for feeding
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the feeding app here
    url(r'', views.feed, name='feed'),

    # Example:
#    url(r'^$', views.home, name='home'),
]
