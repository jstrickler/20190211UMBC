from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# example:
# def home(request):
#     context = { 'message': 'Hello' }
#     return render(request, 'feeding/home.html', context)

def feed(request):
    return HttpResponse("Feeding the wombats")