from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/")
def create_doctor(data: DoctorCreate, db: Session = Depends(get_db)):
    doctor = Doctor(**data.dict())
    db.add(doctor)
    db.commit()
    return {"message": "Doctor added"}

@router.get("/")
def get_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()