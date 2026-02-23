from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from .utils import create_access_token, verify_password, get_password_hash

router = APIRouter(prefix="/auth", tags=["Auth"])

# Simulación de base de datos en memoria
fake_users_db = {}


@router.post("/register")
def register(username: str, email: str, password: str):
    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    hashed_password = get_password_hash(password)

    fake_users_db[username] = {
        "username": username,
        "email": email,
        "password": hashed_password
    }

    return {"msg": "Usuario registrado correctamente"}


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

    if not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")

    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=timedelta(minutes=30)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }