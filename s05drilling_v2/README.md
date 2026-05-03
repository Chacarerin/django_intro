# 🧱 Semana 5 (V2): Herencia Estructural Avanzada

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

El objetivo de esta iteración es solventar la alta duplicación de código vista en ejercicios iniciales. Se asimilan prácticas orientadas a optimizar el mantenimiento de la interfaz de usuario.

## 📌 Contenidos Principales
- **Principio DRY en Frontend:** Concepción y estructuración de un archivo maestro (`base.html`), que engloba elementos invariables como cabeceras, menús de navegación y pies de página.
- **Polimorfismo de Bloques (`{% block %}`):** Definición de "huecos" lógicos en la plantilla base que son sobrescritos o heredados recursivamente por las sub-vistas, reduciendo dramáticamente el peso de los archivos.
- **Servicio de Ficheros Estáticos:** Vinculación controlada del directorio `static/` a través de tags lógicos (`{% load static %}`) para habilitar el consumo de hojas de estilo (CSS) externas e imágenes de soporte.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Arquitectura de Herencia de Django:** Fundamental para escalar proyectos front-end masivos; cualquier modificación estética global puede realizarse alterando un único archivo maestro que luego propaga la actualización a decenas de sub-vistas simultáneamente.

---
*Desarrollado por Rubén Schnettler.*
