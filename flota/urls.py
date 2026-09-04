"""Rutas propias de la aplicación flota."""

from django.urls import path

from . import views


app_name = "flota"

urlpatterns = [
    path("", views.inicio, name="inicio"),
]

