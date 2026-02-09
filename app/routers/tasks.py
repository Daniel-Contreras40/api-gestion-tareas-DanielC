from fastapi import APIRouter
from app.controllers.tasks_controller import get_tasks, create_task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/")
def list_tasks():
    return get_tasks()


@router.post("/", status_code=201)
def add_task(task: dict):
    return create_task(task)