# Introducción a Django y Arquitectura MVT

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Este repositorio documenta el proceso de aprendizaje secuencial y progresivo en el framework **Django**. Contiene ejercicios semanales ("drilling" y "rebound") diseñados para consolidar los conceptos clave de la arquitectura Modelo-Vista-Plantilla (MVT), desde la configuración inicial hasta el despliegue de aplicaciones robustas.

## Catálogo de Módulos

El repositorio está estructurado cronológicamente. Cada subcarpeta contiene un proyecto Django independiente con su propia documentación específica:

* **Semana 1:**
  * `s01drilling`: Configuración inicial del proyecto, creación de apps, rutas básicas (urls) y primeras vistas estáticas.

* **Semanas 5 y 6:**
  * `s05drilling` / `s05drilling_v2`: Profundización en vistas, paso de contexto a las plantillas y herencia de templates.
  * `s06drilling` / `s06rebound`: Integración de formularios (Forms y ModelForms), validación de datos del lado del servidor y manejo de peticiones POST.

* **Semanas 7 y 8:**
  * `s07drilling` / `s07rebound`: Uso avanzado del ORM, relaciones entre modelos y vistas basadas en clases (CBVs).
  * `s08drilling` / `s08rebound`: Implementación de sistemas de autenticación, control de acceso (decorators y mixins) y gestión de sesiones de usuario.

* **Proyectos Integradores:**
  * `proyecto_vehiculos_django`: Catálogo básico demostrando el flujo completo MVT.
  * `site_django` / `web_django`: Aplicaciones con diseño mejorado, integrando archivos estáticos (CSS/JS).
  * `m7rebound_drilling`: (Contiene su propio repositorio con foco avanzado en Base de Datos y PostgreSQL).

## Ejecución de Proyectos

Para levantar cualquier módulo localmente:
1. Navega al directorio deseado.
2. Asegúrate de tener tu entorno virtual activo.
3. Ejecuta las migraciones pertinentes: `python manage.py migrate`.
4. Levanta el servidor: `python manage.py runserver`.

---
*Desarrollado por Rubén Schnettler.*
