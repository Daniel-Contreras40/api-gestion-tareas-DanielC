from fastapi import FastAPI
from app.routers import tasks

app = FastAPI(title="API Gestión de Tareas")

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "API de Gestión de Tareas funcionando correctamente"}