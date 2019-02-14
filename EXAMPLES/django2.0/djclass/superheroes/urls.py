"""
URL Configuration for superheroes
"""
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .models import City, Superhero, Power, Enemy

urlpatterns = [
    # welcome page, no class-based views
    path('', views.home, name='home'),

    # NO view -- don't do this:
    path(
        'genericonly',
        TemplateView.as_view(template_name='generic_only.html'),
        name="genericonly",
    ),

    # generic template rendering
    # with some context (no models)
    path(
        'genericcontext',
        views.GenericContext.as_view(),
        name="genericcontext",
    ),

    # minimal views with models
    path(
        'minimallist',
        views.HeroListViewMinimal.as_view(),
        name="minimallist",
    ),
    path(
        'minimaldetails/<int:pk>',
        views.HeroDetailViewMinimal.as_view(),  # returns a view function from the class
        name="minimaldetails",
    ),

    #
    path(
        'genericcontext',
        views.GenericContext.as_view(),
        name="genericcontext",
    ),
    path(
        'genericlist',
        views.HeroListView.as_view(),
        name="genericlist",
    ),
    url(
        'genericdetail/<int:pk>',
        views.HeroDetailView.as_view(),
        name="genericdetail",
    ),
    path(
        'herocreate',
        views.HeroCreateView.as_view(),
        name="herocreate",
    ),
    path(
        'citycreate',
        views.CityCreateView.as_view(),
        name="citycreate",
    ),
    path(
        'heroupdate/<int:pk>',
        views.HeroUpdateView.as_view(),
        name="heroupdate",
    ),
    path(
        'success', views.SuccessView.as_view(), name="success",
    ),
    path(
        'herotable',
        views.Table.as_view(model=Superhero),
        name="herotable",
    ),
    path(
        'citytable',
        views.Table.as_view(model=City),
        name="citytable",
    ),
    path(
        'powertable',
        views.Table.as_view(model=Power),
        name="powertable",
    ),

]

