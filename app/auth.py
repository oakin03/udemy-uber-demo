from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json

router = APIRouter()


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    id: int
    name: str
    role: str


@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    with open("data/users.json", "r", encoding="utf-8") as f:
        users = json.load(f)

    for user in users:
        if user["email"] == request.email and user["password"] == request.password:
            return {
                "id": user["id"],
                "name": user["name"],
                "role": user["role"]
            }

    raise HTTPException(status_code=401, detail="Email veya şifre hatalı")
