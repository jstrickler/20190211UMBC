"""
URL Configuration for baking
"""
from django.conf.urls import url
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the baking app here

    # Example:
    url(r'', views.home, name='home'),
    # url(r'cake', views.cake, name='cake'),
]
