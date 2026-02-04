from fastapi import APIRouter
from app.auth import verify_user

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    if verify_user(username, password):
        return {"status": "success", "message": "Login successful"}
    return {"status": "failed", "message": "Invalid credentials"}
