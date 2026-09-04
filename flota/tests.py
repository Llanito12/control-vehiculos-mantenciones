from django.test import TestCase, override_settings
from django.urls import reverse


class InicioTests(TestCase):
    def test_inicio_responde_y_muestra_el_proyecto(self) -> None:
        response = self.client.get(reverse("flota:inicio"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Control de Vehículos y Mantenciones")
        self.assertContains(response, "4 módulos planificados")

    @override_settings(DEBUG=False)
    def test_ruta_inexistente_usa_pagina_404_personalizada(self) -> None:
        response = self.client.get("/esta-ruta-no-existe/")

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "errors/404.html")
        self.assertContains(response, "No encontramos esa página", status_code=404)

