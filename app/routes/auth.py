from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserLogin
from app.services.auth_service import authenticate_user
from app.utils.jwt_handler import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)

    if not db_user:
        return {"error": "Invalid credentials"}

    token = create_token({"sub": db_user.username})
    return {"access_token": token}