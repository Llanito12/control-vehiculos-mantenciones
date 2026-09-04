"""Rutas generales del proyecto."""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("flota.urls")),
]

handler404 = "flota.views.custom_404"

