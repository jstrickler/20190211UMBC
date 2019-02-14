from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# example:
# def home(request):
#     context = { 'message': 'Hello' }
#     return render(request, 'welcome/home.html', context)

def index(request):
    return HttpResponse("Welcome to the Cooking site<br/>" + request.method)