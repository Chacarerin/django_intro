# 🛡️ Semana 8 (Rebound): Permisos Granulares y Roles

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

Avance hacia el Control de Acceso Basado en Roles (RBAC), superando la lógica binaria (autenticado vs anónimo) para definir privilegios específicos por grupo de usuarios.

## 📌 Contenidos Principales
- **Asignación de Grupos:** Creación de entidades lógicas (e.g. 'Editores', 'Administradores') y asignación masiva de usuarios para evitar el micro-manejo de privilegios.
- **Permisos a Nivel de Modelo:** Configuración de directrices granulares (add, change, delete, view) atadas específicamente a tablas concretas de la base de datos.
- **Lógica Condicional en Frontend:** Restricción dinámica de la interfaz de usuario (ocultar botones o formularios) evaluando `{% if perms.app_name %}` directamente en el código de la plantilla.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django Permissions System:** La integración nativa de este sistema con el ORM y el panel administrativo garantiza que una restricción de seguridad definida a nivel de modelo sea respetada en todas las capas jerárquicas de la aplicación.

---
*Desarrollado por Rubén Schnettler.*
