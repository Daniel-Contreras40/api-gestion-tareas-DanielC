# API de Gestión de Tareas

## Descripción

Esta API REST permite la gestión de tareas personales y de pequeños equipos, facilitando la creación, organización, asignación y seguimiento de actividades. Su objetivo es ayudar a los usuarios a mejorar su productividad mediante un sistema claro y estructurado para el control de tareas, fechas límite y estados de progreso.

Está dirigida a estudiantes, freelancers y equipos pequeños que requieren una herramienta sencilla y flexible para administrar su trabajo diario. La API proporciona endpoints para manejar usuarios, tareas, proyectos y estados, permitiendo su integración con aplicaciones web, móviles o de escritorio.

---

## Alcance (Scope) y Recursos (MVP)

### Recursos principales:
- **users** → Usuarios del sistema  
- **tasks** → Tareas  
- **projects** → Proyectos o categorías  
- **status** → Estados de las tareas  

---

## Reglas de negocio

- No se permite crear tareas sin título.
- No se puede asignar una fecha límite en el pasado.
- Una tarea solo puede tener un estado válido: `pending`, `in_progress`, `done`.
- No se permite eliminar tareas que estén en estado `in_progress`.
- Un usuario no puede tener más de 10 tareas pendientes al mismo tiempo.

---

## Endpoints planeados (MVP)

### Users
- GET /users
- POST /users

### Tasks
- GET /tasks
- POST /tasks
- PUT /tasks/{id}
- DELETE /tasks/{id}

### Projects
- GET /projects
- POST /projects

---

## Contrato preliminar (ejemplo)

### Endpoint: Crear tarea

**POST /tasks**

**Request JSON:**
```json
{
  "title": "Estudiar FastAPI",
  "description": "Repasar endpoints y routers",
  "due_date": "2026-02-15",
  "status": "pending"
}

