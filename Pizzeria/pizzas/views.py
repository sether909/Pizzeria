from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pizzas(request):
    return HttpResponse("Hello world!")