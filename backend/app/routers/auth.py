from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class RegisterIn(BaseModel):
    username: str
    password: str

@router.post('/register')
def register(data: RegisterIn):
    # Placeholder: implement proper password hashing and user storage
    return {"message": "register endpoint - implement persistence"}

class LoginIn(BaseModel):
    username: str
    password: str

@router.post('/login')
def login(data: LoginIn):
    # Placeholder: return JWT token (implement real auth)
    if data.username == "admin" and data.password == "password":
        return {"access_token": "fake-jwt-token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
