# Datos simulados (mock)
tasks_db = [
    {
        "id": 1,
        "title": "Hacer tarea de backend",
        "description": "Terminar proyecto API REST",
        "status": "pending"
    },
    {
        "id": 2,
        "title": "Estudiar para examen",
        "description": "Repasar FastAPI",
        "status": "in_progress"
    }
]


def get_tasks():
    return tasks_db


def create_task(task: dict):
    new_id = len(tasks_db) + 1
    task["id"] = new_id
    tasks_db.append(task)

    return {
        "message": "Tarea creada correctamente",
        "task": task
    }