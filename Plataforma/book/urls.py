
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

def mi_mista(xx):
    return HttpResponse("<h1>hola!!! esta es mi vista<h1/>")

urlpatterns = [
    path("", mi_mista)
]
