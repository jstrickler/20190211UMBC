from django.http import HttpResponse
from .models import Superhero

def home(request):
    return HttpResponse("Welcome to my app")

def hero(request, hero_name):
    s = Superhero.objects.get(name=hero_name)
    return HttpResponse(
        "{} is really {}".format(s.secret_identity, s.name)
    )

def herorepeat(request, hero_name, repeat):
    s = Superhero.objects.get(name=hero_name)
    multi_hero = s.name * repeat
    return HttpResponse(multi_hero)

