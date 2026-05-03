# 🔐 Semana 8: Autenticación y Autorización

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

El módulo se adentra en la seguridad de aplicaciones web, implementando el robusto sistema de usuarios (`django.contrib.auth`) para proteger recursos y personalizar la experiencia por sesión.

## 📌 Contenidos Principales
- **Gestión de Sesiones:** Construcción de flujos completos de inicio de sesión (Login), cierre (Logout) y registro de nuevos usuarios, manejando la encriptación asimétrica de contraseñas.
- **Protección de Endpoints:** Uso del decorador `@login_required` para interceptar peticiones a vistas funcionales y redireccionar clientes no autorizados.
- **Seguridad en CBVs:** Implementación equivalente del `LoginRequiredMixin` para asegurar arquitecturas basadas en clases.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django Auth Framework:** Módulo maduro y auditado criptográficamente que gestiona el hasheo de contraseñas (mediante algoritmos como PBKDF2), la validación algorítmica de complejidad y el mantenimiento de la sesión basada en cookies de forma completamente transparente.

---
*Desarrollado por Rubén Schnettler.*
