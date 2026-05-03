# 🛠️ Semana 7 (Rebound): Django Admin y CBVs

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

Este ejercicio introduce dos de las herramientas más potentes del ecosistema para la reducción de código repetitivo (Boilerplate): El panel administrativo y las Vistas Basadas en Clases.

## 📌 Contenidos Principales
- **Personalización Administrativa (`admin.py`):** Configuración de la clase `ModelAdmin` para modificar la visualización de los registros en el backend, añadiendo barras de búsqueda, filtros laterales e interfaces tabulares.
- **Vistas Basadas en Clases (CBVs):** Refactorización de la lógica imperativa de funciones a un paradigma declarativo, heredando de clases genéricas como `ListView` y `DetailView` que encapsulan los patrones de diseño web más comunes.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django Class-Based Views:** Patrón arquitectónico que promueve el principio Abierto/Cerrado (Open/Closed Principle) del diseño de software, permitiendo extender la funcionalidad genérica de una vista sobrescribiendo métodos específicos (`get_context_data`, `get_queryset`) en lugar de reescribirla.

---
*Desarrollado por Rubén Schnettler.*
