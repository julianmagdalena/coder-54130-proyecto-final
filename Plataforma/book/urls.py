
from django.contrib import admin
from django.urls import path

from .views import home_view, list_view

urlpatterns = [
    path("", home_view),
    path("lista/", list_view)
]
