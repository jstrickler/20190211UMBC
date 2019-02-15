"""
URL Configuration for apiv1
"""
from django.conf.urls import url
from django.urls import path
from . import views   # import views from app
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Superhero API')

urlpatterns = [
    # add url patterns for the apiv1 app here

    # Example:
    path('', schema_view, name='schema'),
    path('superhero', views.superhero, name='superhero'),
    path(
        'superhero/<int:pk>',
        views.superhero_detail,
        name='superherodetail'
    ),
    path(
        'enemy', views.EnemyList.as_view(), name='enemy'
    ),
    path(
        'enemy/<int:pk>',
        views.EnemyDetail.as_view(),
        name='enemydetail'
    )
]
