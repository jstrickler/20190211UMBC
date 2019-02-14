"""
URL Configuration for my_app
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the my_app app here

    # Example:
   url(r'^$', views.home, name='home'),
]
