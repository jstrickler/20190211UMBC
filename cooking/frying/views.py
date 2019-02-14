from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# example:
# def home(request):
#     context = { 'message': 'Hello' }
#     return render(request, 'frying/home.html', context)

def home(request):
    return HttpResponse("Welcome to Frying")