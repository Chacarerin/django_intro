# 🚗 Proyecto Catálogo de Vehículos

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

Proyecto que funge como hito integrador. A diferencia de ejercicios aislados, esta aplicación orquesta de forma completa y simultánea todas las capas de la arquitectura MVT (Modelo-Vista-Plantilla).

## 📌 Contenidos Principales
- **Cohesión Estructural (MVT):** Demostración de cómo un Modelo interroga la base de datos, transfiere el conjunto de resultados a una Vista, y cómo esta última formatea el contexto final que inyecta en el Template HTML.
- **Captura Transaccional Segura:** Empleo de componentes formales (ModelForms) que automatizan validaciones a nivel de backend y mitigan el riesgo de inyección de datos corruptos antes de impactar el catálogo.
- **Jerarquía de Vistas (List/Detail):** Patrón fundacional en el desarrollo web, presentando un inventario resumido navegable hacia las características microscópicas de un vehículo en particular.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django Form Engine:** Se estudia académicamente la abstracción de campos HTML y su vinculación estricta con las restricciones del modelo original, reduciendo el riesgo de errores de validación humanos.

---
*Desarrollado por Rubén Schnettler.*
