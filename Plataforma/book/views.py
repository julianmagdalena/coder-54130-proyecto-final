from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>hola!!! esta es mi vista<h1/>")

def list_view(request):
    return HttpResponse("<h3>Esta es la lista de juegos<h3/>")