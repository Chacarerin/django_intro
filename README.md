# 🚀 Introducción a Django

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Repositorio destinado a los primeros pasos y proyectos iniciales utilizando el framework web **Django**. 

Encontrarás aplicaciones simples y ejercicios guiados que cubren los fundamentos de la arquitectura MVT (Model-View-Template).

## 🗂️ Proyectos Incluidos

### 1. `proyecto_vehiculos_django`
Aplicación básica para el registro y visualización de un catálogo de vehículos. Demuestra el uso de Modelos simples, vistas basadas en funciones/clases y el sistema de plantillas de Django.

### 2. `s01drilling`
Ejercicio práctico de la primera semana de aprendizaje. Configuración inicial de un proyecto Django, creación de apps, rutas básicas (urls) y las primeras vistas.

### 3. `m7rebound_drilling`
*(Nota: Este módulo contiene su propio repositorio con foco en Base de Datos y ORM).*

---

## 🛠️ Cómo Ejecutar

Para correr cualquiera de los proyectos:
1. Clona este repositorio.
2. Navega al directorio del proyecto (por ejemplo `cd proyecto_vehiculos_django`).
3. Crea tu entorno virtual y actívalo.
4. Instala Django si no está instalado globalmente (`pip install django`).
5. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```
6. Levanta el servidor:
   ```bash
   python manage.py runserver
   ```
   
---
*Desarrollado con ❤️ por Rubén Schnettler*
