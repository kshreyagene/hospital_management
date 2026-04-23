from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientCreate

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/")
def create_patient(data: PatientCreate, db: Session = Depends(get_db)):
    patient = Patient(**data.dict())
    db.add(patient)
    db.commit()
    return {"message": "Patient created"}

@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()