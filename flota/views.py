"""Vistas de la aplicación flota."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


NOMBRE_PROYECTO: str = "Control de Vehículos y Mantenciones"
DESCRIPCION: str = (
    "Una plataforma para centralizar vehículos, conductores, talleres e historial "
    "de mantenimiento de una flota empresarial."
)
MODULOS_PLANIFICADOS: list[str] = [
    "Vehículos",
    "Conductores",
    "Talleres",
    "Mantenciones",
]


def inicio(request: HttpRequest) -> HttpResponse:
    """Muestra la bienvenida y datos básicos del proyecto asignado."""
    cantidad_modulos = len(MODULOS_PLANIFICADOS)

    if cantidad_modulos > 0:
        estado = f"Proyecto preparado con {cantidad_modulos} módulos planificados."
    else:
        estado = "Aún no existen módulos planificados."

    contexto = {
        "nombre_proyecto": NOMBRE_PROYECTO,
        "descripcion": DESCRIPCION,
        "modulos": MODULOS_PLANIFICADOS,
        "cantidad_modulos": cantidad_modulos,
        "estado": estado,
    }
    return render(request, "flota/inicio.html", contexto)


def custom_404(
    request: HttpRequest, exception: Exception | None = None
) -> HttpResponse:
    """Entrega una respuesta propia cuando Django no encuentra una ruta."""
    contexto = {
        "ruta_solicitada": request.path,
        "nombre_proyecto": NOMBRE_PROYECTO,
    }
    return render(request, "errors/404.html", contexto, status=404)

