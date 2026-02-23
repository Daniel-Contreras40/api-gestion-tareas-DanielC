from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext

from .auth_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Simulación de BD (luego la conectamos a la real)
fake_users_db = []

class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

@router.post("/register")
def register(user: UserRegister):
    hashed_password = get_password_hash(user.password)
    fake_users_db.append({
        "email": user.email,
        "password": hashed_password
    })
    return {"message": "Usuario registrado correctamente"}

@router.post("/login")
def login(user: UserLogin):
    for u in fake_users_db:
        if u["email"] == user.email and verify_password(user.password, u["password"]):
            token = create_access_token({"sub": user.email})
            return {"access_token": token}

    raise HTTPException(status_code=401, detail="Credenciales incorrectas")