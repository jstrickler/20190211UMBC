"""
URL Configuration for superheroes
"""
from django.conf.urls import url  # django 1.x
from django.urls import path      # django 2.x
from . import views   # import views from app
from . import views404
from . import viewsbasictemplate
from . import viewstemplate
from . import viewsqueries

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path("herorepeat/<str:hero_name>/<int:repeat>", views.herorepeat, name="herorepeat"),
#    url(r'^hero/(?P<hero_name>.*)', views.hero, name="hero"),
    path("hero/<str:hero_name>", views.hero, name="hero"),
    url(r'^hero404x/(?P<hero_name>.*)', views404.hero404, name="hero404"),
    url(r'^hero404sc/(?P<hero_name>.*)', views404.hero404sc, name="hero404sc"),
    url(
        r'^herotemplate101/(?P<hero_name>.*)',
        viewsbasictemplate.hero_basic_template,
        name="herobasictemplate",
    ),
    url(
        r'^herohardway/(?P<hero_name>.*)',
        viewstemplate.hero_hard_way,
        name="herohardway",
    ),
    url(
        r'^heroeasyway/(?P<hero_name>.*)',
        viewstemplate.hero_easy_way,
        name="heroeasyway",
    ),
    url(
        r'^herolookups/(?P<hero_name>.*)',
        viewstemplate.hero_lookups,
        name="herolookups",
    ),
    url(
        r'^herofilters/(?P<hero_name>.*)',
        viewstemplate.hero_filters,
        name="herofilters",
    ),
    url(
        r'^herotags/(?P<hero_name>.*)',
        viewstemplate.hero_tags,
        name="herotags",
    ),
    url(
        r'^herodetails/(?P<hero_name>.*)',
        viewstemplate.hero_details,
        name="herodetails",
    ),
    url(
        r'^heroescape/(?P<hero_name>.*)',
        viewstemplate.hero_escape,
        name="heroescape",
    ),
    url(
        r'^herourls',
        viewstemplate.hero_urls,
        name="herourls",
    ),
    url(
        r'^herostatic/(?P<hero_name>.*)',
        viewstemplate.hero_static,
        name="herostatic",
    ),
    url(
        r'^heroqueries',
        viewsqueries.hero_queries,
        name="heroqueries",
    ),
]

