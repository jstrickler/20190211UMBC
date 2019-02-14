from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# example:
# def home(request):
#     context = { 'message': 'Hello' }
#     return render(request, 'wrangle/home.html', context)
def wrangle(request):
    return HttpResponse("Wrangling me some wombats")

