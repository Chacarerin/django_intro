# 📝 Semana 6: Validación y Captura de Formularios

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

Punto de inflexión hacia aplicaciones interactivas. El módulo explora teóricamente cómo Django recibe, esteriliza y procesa los flujos de información bidireccional enviados desde el cliente mediante el protocolo HTTP.

## 📌 Contenidos Principales
- **Abstracción Algorítmica de Formularios:** Uso de la clase base `forms.Form` para modelar y tipificar en Python las estructuras que se renderizarán como componentes HTML complejos (input tags, labels).
- **Procesamiento Condicional de Peticiones:** Segmentación de la respuesta basándose en verbos HTTP (evaluando `request.method == 'POST'` frente a peticiones estándar 'GET').
- **Rutinas de Validación Intrinseca:** Uso del método `form.is_valid()` y la recolección de datos higienizados a través de `cleaned_data` para proteger el servidor de cargas perjudiciales.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django Forms Library:** Una librería de defensa y estructuración robusta, diseñada para mitigar fallas de seguridad humanas al automatizar tareas tediosas como el escapado de caracteres, validaciones Regex y la serialización temporal de variables incompletas.

---
*Desarrollado por Rubén Schnettler.*
