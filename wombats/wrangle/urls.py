"""
URL Configuration for wrangle
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the wrangle app here

    # Example:
    url(r'', views.wrangle, name='wrangle'),
]
