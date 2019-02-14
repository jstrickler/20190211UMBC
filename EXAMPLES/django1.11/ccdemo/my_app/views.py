from django.shortcuts import render

# Create your views here.

# example:
def home(request):
    context = { 'message': 'Welcome to an app created with cookiecutter-django1.11-app' }
    return render(request, 'home.html', context)
