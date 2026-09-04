# Control de Vehículos y Mantenciones

Proyecto individual de **Esteban Mauricio Llanos Sandoval** para la Evaluación 1 de Programación Backend (INACAP, 2026).

La aplicación establece la base técnica de una plataforma destinada a centralizar la información de vehículos, conductores, talleres y mantenciones de una flota empresarial. Esta primera entrega incluye el núcleo Django, una aplicación con rutas propias, una bienvenida temática y una página 404 personalizada.

## Requisitos

- Python 3.12 o compatible
- Git

## Instalación en Windows PowerShell

```powershell
git clone URL_DEL_REPOSITORIO
cd control-vehiculos-mantenciones
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Luego abre `http://127.0.0.1:8000/`. Para comprobar el error personalizado, visita `http://127.0.0.1:8000/ruta-inexistente/`.

## Comprobaciones

```powershell
python manage.py check
python manage.py test
```

## Estructura principal

- `config/`: configuración general y conexión de rutas del proyecto.
- `flota/`: aplicación particular, con vistas, rutas y pruebas.
- `templates/flota/`: plantillas de la bienvenida.
- `templates/errors/404.html`: página de error personalizada.
- `requirements.txt`: dependencias exactas del proyecto.

El ambiente `.venv`, la base local y los archivos sensibles quedan excluidos mediante `.gitignore`.

