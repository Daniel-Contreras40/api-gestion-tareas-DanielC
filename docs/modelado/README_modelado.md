# Modelado del Sistema — API Gestión de Tareas

## Descripción del dominio

El sistema resuelve la necesidad de gestionar tareas personales y de pequeños equipos, permitiendo organizar actividades, asignarlas a usuarios y agruparlas dentro de proyectos.

El objetivo principal es facilitar el control del trabajo diario, mejorar la productividad y proporcionar una estructura clara para el seguimiento del progreso de las tareas.

---

## Entidades principales

- **User**: representa a los usuarios del sistema.
- **Task**: entidad central del negocio, representa una tarea.
- **Project**: agrupa tareas relacionadas.
- **TaskProject**: tabla puente para la relación N–N entre tareas y proyectos.

---

## Decisiones clave

- Se eligió una arquitectura con separación clara entre modelos, rutas y controladores.
- Se implementó una relación N–N entre tareas y proyectos para permitir que una tarea pertenezca a múltiples proyectos.
- Se definieron timestamps para auditoría básica del sistema.
- Se estableció la restricción UNIQUE en el email del usuario para evitar duplicados.

---

## Supuestos

- Un usuario puede crear múltiples tareas.
- Una tarea puede pertenecer a uno o varios proyectos.
- Los estados se manejan mediante una cadena controlada desde la lógica del sistema.
- El sistema está orientado a pequeños equipos con bajo volumen de usuarios.

---

## Relaciones implementadas

- **User 1 — N Task**
- **Task N — N Project** mediante tabla intermedia

---

## Tecnologías

- FastAPI
- SQLAlchemy ORM
- PostgreSQL (planeado)