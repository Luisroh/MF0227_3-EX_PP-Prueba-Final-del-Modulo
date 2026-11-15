# 🛠️ HelpDesk — Sistema de Gestión de Incidencias Técnicas

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completado-brightgreen)

Sistema web de gestión de incidencias técnicas (HelpDesk) desarrollado como
proyecto de evaluación del módulo **MF0227_3 — Programación orientada a objetos**
(UF2404, UF2405 y UF2406) del certificado **IFCD0112**.

El proyecto integra en un mismo repositorio:

- Un **módulo de POO puro en Python** (`core_modelos.py`) que modela la lógica
  de negocio de los tickets con encapsulamiento, herencia, polimorfismo y
  excepciones personalizadas.
- Una **aplicación web Django** (`helpdesk_project` + app `incidencias`) con
  modelos ORM, panel de administración, vistas basadas en clases, formularios
  y plantillas con herencia y Bootstrap.
- Un **flujo de trabajo profesional** con Git (ramas `main` y `desarrollo`,
  commits atómicos y descriptivos), entorno virtual, `requirements.txt`,
  documentación y plan de pruebas.

---

## 📑 Índice

- [🛠️ HelpDesk — Sistema de Gestión de Incidencias Técnicas](#️-helpdesk--sistema-de-gestión-de-incidencias-técnicas)
  - [📑 Índice](#-índice)
  - [🎯 Contexto y objetivos](#-contexto-y-objetivos)
  - [🧰 Tecnologías utilizadas](#-tecnologías-utilizadas)
  - [📋 Requisitos previos](#-requisitos-previos)
  - [🚀 Instalación y despliegue local](#-instalación-y-despliegue-local)
    - [1. Clonar el repositorio](#1-clonar-el-repositorio)
    - [2. Crear y activar el entorno virtual](#2-crear-y-activar-el-entorno-virtual)
    - [3. Instalar dependencias](#3-instalar-dependencias)
    - [4. Aplicar migraciones](#4-aplicar-migraciones)
    - [5. (Opcional pero recomendado) Crear superusuario](#5-opcional-pero-recomendado-crear-superusuario)
    - [6. Levantar el servidor de desarrollo](#6-levantar-el-servidor-de-desarrollo)
    - [7. Ejecutar el módulo de POO (independiente de Django)](#7-ejecutar-el-módulo-de-poo-independiente-de-django)
  - [📁 Estructura del proyecto](#-estructura-del-proyecto)
  - [🏗️ Arquitectura y relación entre UF](#️-arquitectura-y-relación-entre-uf)
    - [UF2404 — Principios de POO (30%)](#uf2404--principios-de-poo-30)
    - [UF2405 — Desarrollo web y bases de datos (40%)](#uf2405--desarrollo-web-y-bases-de-datos-40)
    - [UF2406 — Ciclo de vida, Git y documentación (30%)](#uf2406--ciclo-de-vida-git-y-documentación-30)
    - [Diagrama de relación](#diagrama-de-relación)
  - [🗃️ Modelo de datos](#️-modelo-de-datos)
    - [`Tecnico`](#tecnico)
    - [`Incidencia`](#incidencia)
  - [🌐 Rutas y funcionalidades](#-rutas-y-funcionalidades)
  - [🖥️ Uso de la aplicación](#️-uso-de-la-aplicación)
  - [🧪 Plan de pruebas / Validación](#-plan-de-pruebas--validación)
  - [🌿 Control de versiones (Git)](#-control-de-versiones-git)
    - [Convención de mensajes de commit](#convención-de-mensajes-de-commit)
    - [Historial esperado (ejemplo)](#historial-esperado-ejemplo)
  - [🧠 Decisiones de diseño](#-decisiones-de-diseño)
  - [🔮 Mejoras futuras](#-mejoras-futuras)
  - [👤 Autoría](#-autoría)
  - [📄 Licencia](#-licencia)

---

## 🎯 Contexto y objetivos

Se requiere desarrollar el **núcleo funcional y la estructura inicial** de un
Sistema de Gestión de Incidencias Técnicas (HelpDesk) para una empresa
simulada. El desarrollo debe aplicar:

- **Buenas prácticas de POO** (UF2404): encapsulamiento, herencia,
  polimorfismo, excepciones personalizadas.
- **Entorno web robusto con Django y ORM** (UF2405): modelos, migraciones,
  admin, vistas, formularios y plantillas.
- **Control de versiones y documentación** (UF2406): Git con ramas y commits
  atómicos, `requirements.txt`, `README.md` y plan de pruebas.

---

## 🧰 Tecnologías utilizadas

| Tecnología | Versión | Uso |
|------------|---------|-----|
| Python     | 3.11+   | Lenguaje principal |
| Django     | 5.x     | Framework web y ORM |
| SQLite     | 3       | Base de datos por defecto (desarrollo) |
| Bootstrap  | 5.3     | Estilos de las plantillas |
| Git        | 2.x     | Control de versiones |
| venv       | stdlib  | Entorno virtual aislado |

Dependencias exactas: ver [`requirements.txt`](./requirements.txt).

---

## 📋 Requisitos previos

Antes de empezar, asegúrate de tener instalado:

- **Python 3.11 o superior** → `python --version`
- **pip** actualizado → `python -m pip install --upgrade pip`
- **Git** → `git --version`
- (Opcional) Un editor como VS Code o PyCharm.

---

## 🚀 Instalación y despliegue local

Sigue estos pasos **en orden** desde la raíz del proyecto:

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd helpdesk_project_root
```

### 2. Crear y activar el entorno virtual

**Windows (PowerShell / CMD):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> Sabrás que el entorno está activo porque el prompt mostrará `(venv)` al
> principio de la línea.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. (Opcional pero recomendado) Crear superusuario

Permite acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```
Introduce nombre de usuario, email y contraseña cuando se solicite.

### 6. Levantar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre en el navegador:

- Aplicación web → <http://127.0.0.1:8000/incidencias/>
- Panel de administración → <http://127.0.0.1:8000/admin/>

### 7. Ejecutar el módulo de POO (independiente de Django)

```bash
python core_modelos.py
```

Deberías ver por consola los SLA calculados y la captura de la excepción
`EstadoInvalidoError`.

---

## 📁 Estructura del proyecto

```
helpdesk_project_root/
│
├── core_modelos.py              # Bloque 1 — POO pura (UF2404)
├── manage.py                    # Utilidad de gestión de Django
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este documento
├── pruebas.txt                  # Plan de pruebas ejecutado (UF2406)
├── .gitignore                   # Excluye venv, __pycache__, db.sqlite3, etc.
│
├── helpdesk_project/            # Configuración del proyecto Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── incidencias/                 # App Django (UF2405)
│   ├── __init__.py
│   ├── admin.py                 # Registro de modelos con list_display, filtros y search
│   ├── apps.py
│   ├── forms.py                 # IncidenciaForm (ModelForm)
│   ├── models.py                # Tecnico e Incidencia
│   ├── urls.py                  # Rutas de la app
│   ├── views.py                 # ListView y CreateView
│   ├── migrations/
│   │   └── 0001_initial.py
│   └── tests.py
│
└── templates/                   # Plantillas HTML (herencia + Bootstrap)
    ├── base.html
    └── incidencias/
        ├── lista.html
        └── formulario.html
```

---

## 🏗️ Arquitectura y relación entre UF

El proyecto está diseñado en **tres capas claramente diferenciadas** que se
corresponden con las tres unidades formativas evaluadas:

### UF2404 — Principios de POO (30%)

`core_modelos.py` implementa el **modelo de dominio puro** sin dependencia
de Django:

- `TicketTecnico`: clase base con atributos protegidos (`_id`, `_titulo`,
  `_estado`, `_prioridad`) y método `cambiar_estado()` que valida
  transiciones lógicas mediante la tabla `_TRANSICIONES`.
- `TicketHardware` y `TicketSoftware`: subclases que añaden atributos
  específicos (`componente`, `sistema_operativo`) y **sobrescriben**
  `calcular_sla()` con tablas de SLA distintas por tipo y prioridad
  (polimorfismo).
- `EstadoInvalidoError`: excepción personalizada que se lanza cuando se
  intenta una transición no permitida (p. ej. `Cerrado → En Proceso`).

Este módulo es **autónomo**: se puede ejecutar con `python core_modelos.py`
sin necesidad de Django, demostrando la separación entre lógica de negocio
y capa web.

### UF2405 — Desarrollo web y bases de datos (40%)

La app `incidencias` implementa la **capa web y de persistencia**:

- `models.py`: define `Tecnico` e `Incidencia` con `ForeignKey`, campos
  `choices` para `estado` y `prioridad`, y `fecha_creacion` automática.
- `admin.py`: registra ambos modelos con `list_display`, `list_filter` y
  `search_fields` para facilitar la gestión.
- `forms.py`: `IncidenciaForm` como `ModelForm` reutilizable.
- `views.py`: `IncidenciaListView` (hereda de `ListView`) y
  `IncidenciaCreateView` (hereda de `CreateView`).
- `templates/`: `base.html` con herencia y Bootstrap, del que heredan
  `lista.html` y `formulario.html`.

### UF2406 — Ciclo de vida, Git y documentación (30%)

- **Git**: ramas `main` y `desarrollo`, commits atómicos con mensajes
  descriptivos siguiendo convención tipo `feat:`, `docs:`, `chore:`.
- **`requirements.txt`**: dependencias fijadas.
- **`README.md`**: este documento.
- **`pruebas.txt`**: 3 casos de prueba funcionales ejecutados y verificados.

### Diagrama de relación

```
┌─────────────────────┐         ┌──────────────────────┐
│  core_modelos.py    │         │  incidencias/models  │
│  (UF2404 · POO)     │         │  (UF2405 · ORM)      │
│                     │         │                      │
│  TicketTecnico      │  lógica │  Tecnico             │
│   ├─ TicketHardware │  ────►  │  Incidencia          │
│   └─ TicketSoftware │  negocio│   ├─ estado (choices)│
│  EstadoInvalidoError│         │   ├─ prioridad       │
└─────────────────────┘         │   └─ tecnico (FK)    │
                                └──────────┬───────────┘
                                           │
                                ┌──────────▼───────────┐
                                │  views / forms /     │
                                │  templates (UF2405)  │
                                └──────────┬───────────┘
                                           │
                                ┌──────────▼───────────┐
                                │  Git · README ·      │
                                │  pruebas (UF2406)    │
                                └──────────────────────┘
```

---

## 🗃️ Modelo de datos

### `Tecnico`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | AutoField | PK autogenerada |
| `nombre` | CharField(100) | Nombre completo del técnico |
| `especialidad` | CharField(100) | Área de especialización |
| `email` | EmailField | Correo de contacto |

### `Incidencia`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | AutoField | PK autogenerada |
| `titulo` | CharField(200) | Título breve de la incidencia |
| `descripcion` | TextField | Detalle del problema |
| `fecha_creacion` | DateTimeField | Auto (`auto_now_add=True`) |
| `estado` | CharField(20) + choices | `abierta`, `en_proceso`, `cerrada` |
| `prioridad` | CharField(10) + choices | `alta`, `media`, `baja` |
| `tecnico` | ForeignKey(Tecnico) | `on_delete=SET_NULL`, `null=True` |

**Relación:** una `Incidencia` puede tener asignado un `Tecnico`
(ForeignKey). Varias incidencias pueden compartir el mismo técnico.

---

## 🌐 Rutas y funcionalidades

| Método | Ruta | Vista | Descripción |
|--------|------|-------|-------------|
| GET | `/incidencias/` | `IncidenciaListView` | Lista todas las incidencias |
| GET/POST | `/incidencias/nueva/` | `IncidenciaCreateView` | Formulario de alta |
| GET | `/admin/` | Django Admin | Gestión completa de modelos |

---

## 🖥️ Uso de la aplicación

1. Levanta el servidor (`python manage.py runserver`).
2. Accede a `/admin/` con el superusuario y **crea primero un `Tecnico`**.
3. Ve a `/incidencias/nueva/` y **registra una incidencia** asignándole un
   técnico.
4. Vuelve a `/incidencias/` para verla listada con su estado y prioridad
   traducidos (gracias a `get_estado_display` / `get_prioridad_display`).
5. En `/admin/` puedes filtrar por estado y buscar por título o nombre de
   técnico.

---

## 🧪 Plan de pruebas / Validación

Los 3 casos de prueba funcionales ejecutados se detallan en
[`pruebas.txt`](./pruebas.txt). Resumen:

| # | Caso | Resultado esperado | Resultado obtenido |
|---|------|--------------------|--------------------|
| 1 | Transición válida de estado en POO (`Abierto → En Proceso`) | Cambia sin excepción | ✅ OK |
| 2 | Transición inválida en POO (`Cerrado → En Proceso`) | Lanza `EstadoInvalidoError` | ✅ OK (capturada) |
| 3 | Formulario web con campos vacíos | Django muestra error de validación | ✅ OK |

---

## 🌿 Control de versiones (Git)

El repositorio sigue un flujo de trabajo estructurado:

- **Rama `main`**: versión estable / entrega final.
- **Rama `desarrollo`**: rama de trabajo donde se integran los commits
  atómicos de cada bloque.

### Convención de mensajes de commit

```
feat(poo):        nuevas funcionalidades de POO
feat(django):     nuevas funcionalidades Django
feat(admin):      cambios en el panel de administración
feat(views):      vistas, formularios o plantillas
docs:             documentación (README, pruebas.txt)
chore:            tareas de mantenimiento (gitignore, requirements)
fix:              corrección de errores
```

### Historial esperado (ejemplo)

```
* chore: final packaging - delivery v1.0 ready
* docs: add README and pruebas.txt with test cases
* feat(views): add ListView and CreateView with base template inheritance
* feat(admin): register models with list_display, filters and search_fields
* feat(django): add Tecnico and Incidencia models with choices and FK
* feat(poo): implement TicketTecnico base class with inheritance and polymorphism
* chore: add requirements.txt with Django dependency
* chore: initial commit with gitignore
```

---

## 🧠 Decisiones de diseño

- **Separación POO / Django**: `core_modelos.py` no importa Django para
  demostrar que la lógica de negocio es independiente del framework.
- **`ForeignKey` en lugar de `OneToOne`**: un técnico puede atender varias
  incidencias; `ForeignKey` refleja mejor la realidad.
- **`on_delete=SET_NULL`**: si se elimina un técnico, la incidencia no se
  borra, solo queda sin asignar.
- **`choices` en `estado` y `prioridad`**: garantiza integridad a nivel de
  formulario y permite usar `get_*_display` en plantillas.
- **CBV (`ListView`/`CreateView`)**: menos código repetido y más alineado con
  las buenas prácticas de Django.
- **Herencia de plantillas**: `base.html` centraliza navbar y Bootstrap;
  las demás plantillas solo definen el bloque `content`.

---

## 🔮 Mejoras futuras

- Autenticación de usuarios y roles (técnico vs. cliente).
- API REST con Django REST Framework.
- Filtros de búsqueda en la lista (por estado/prioridad).
- Paginación en el `ListView`.
- Tests automáticos con `pytest-django` y cobertura.
- Despliegue en producción (PostgreSQL + Gunicorn + Nginx).

---

## 👤 Autoría

- **Alumno/a:** Luis Robert Huertas Araya
- **Curso:** 25/FOAP/781/0195027/001
- **Módulo:** MF0227_3 — Programación orientada a objetos
- **Formador:** Oscar Burgos

---

## 📄 Licencia

Proyecto académico desarrollado con fines formativos. Distribuido bajo
licencia **MIT** para uso educativo.