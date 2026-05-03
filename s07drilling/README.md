# 🗄️ Semana 7: ORM y Relaciones de Datos

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

El paradigma relacional de bases de datos se aborda desde la perspectiva de la Programación Orientada a Objetos. El objetivo es diseñar esquemas normalizados utilizando el Object-Relational Mapping (ORM) integrado.

## 📌 Contenidos Principales
- **Modelado de Entidades:** Traducción de reglas de negocio a clases de Python, definiendo atributos (campos) y restricciones nativas (longitud, unicidad).
- **Relaciones Estructurales:** Implementación de claves foráneas `ForeignKey` y `ManyToManyField` para vincular información atómicamente, asegurando la integridad referencial (e.g. cascadas de eliminación con `on_delete=models.CASCADE`).
- **Consultas Interactivas (QuerySets):** Extracción de datos aplicando filtros avanzados a través de la terminal interactiva interactiva `manage.py shell`, comprendiendo la evaluación perezosa (*Lazy Evaluation*) de Django.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django ORM:** Abstracción que traduce métodos en sentencias SQL eficientes y parametrizadas, protegiendo por diseño el aplicativo contra ataques de inyección SQL (SQLi).

---
*Desarrollado por Rubén Schnettler.*
