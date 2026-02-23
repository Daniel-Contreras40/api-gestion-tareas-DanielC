# ------------------ IMPORTACIONES PRINCIPALES ------------------

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

# ------------------ IMPORTACIONES DE BASE DE DATOS ------------------

from app.db.database import Base, engine
from app.models import user

# ------------------ IMPORTACIÓN DE RUTAS ------------------

from app.auth.routes import router as auth_router

# ------------------ CONFIGURACIÓN JWT PARA SWAGGER ------------------

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# ------------------ CREAR TABLAS ------------------

Base.metadata.create_all(bind=engine)

# ------------------ CREAR APLICACIÓN ------------------

app = FastAPI(
    title="API Gestión de Tareas",
    description="API REST con autenticación JWT",
    version="1.0"
)

# ------------------ REGISTRAR RUTAS ------------------

app.include_router(auth_router)

# ------------------ CONFIGURACIÓN DE CORS ------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ ENDPOINT DE PRUEBA PROTEGIDO ------------------

@app.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):
    return {
        "message": "Acceso permitido con JWT",
        "token": token
    }