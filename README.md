# HelpDesk — Sistema de Gestión de Incidencias Técnicas

## Instalación y despliegue local

1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`
3. Activar: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (Linux/Mac)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Ejecutar migraciones: `python manage.py migrate`
6. Crear superusuario (opcional): `python manage.py createsuperuser`
7. Levantar servidor: `python manage.py runserver`

Acceder a: `http://127.0.0.1:8000/incidencias/` y `http://127.0.0.1:8000/admin/`

## Arquitectura del proyecto

- **UF2404 (POO):** `core_modelos.py` implementa la jerarquía de tickets con encapsulamiento, herencia y polimorfismo.
- **UF2405 (Django/ORM):** La app `incidencias` contiene modelos (`Tecnico`, `Incidencia`), admin personalizado, vistas basadas en clases y plantillas con herencia.
- **UF2406 (Ciclo de vida):** Control de versiones con Git (ramas `main` y `desarrollo`), `requirements.txt` y documentación.

## Plan de pruebas

Ver `pruebas.txt`.