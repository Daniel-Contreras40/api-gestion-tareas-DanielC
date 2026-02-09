from fastapi import FastAPI

app = FastAPI(title="API Gestión de Tareas")

@app.get("/")
def root():
    return {"message": "API de Gestión de Tareas funcionando correctamente"}