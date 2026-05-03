# 🎨 Semana 5: Vistas Dinámicas y Sistema de Plantillas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

Se produce la transición desde respuestas de texto plano (HttpResponse) a la construcción de documentos estructurados HTML. El foco académico yace en la inyección segura de variables de memoria al código de renderizado final.

## 📌 Contenidos Principales
- **Intersección Contextual:** Uso riguroso de diccionarios contextuales (Context) mediante la función `render()`. Esto permite la separación de preocupaciones: el back-end procesa, el front-end formatea.
- **Lógica en el Marcaje:** Introducción e implementación de condicionales y bucles iterativos (`{% if %}`, `{% for %}`) directamente sobre plantillas HTML, otorgándole inteligencia al archivo estático.
- **Configuración de Directorios DTL:** Manipulación de variables estructurales en `settings.py` (`TEMPLATES_DIRS`) para unificar la búsqueda jerárquica de recursos visuales.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django Template Language (DTL):** Motor de plantillas nativo de Django, diseñado estructuralmente para evitar inyección de código severo en la capa de vista y obligar al desarrollador a trasladar el peso lógico hacia Python.

---
*Desarrollado por Rubén Schnettler.*
