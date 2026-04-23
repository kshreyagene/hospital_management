from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/")
def create_appointment(data: AppointmentCreate, db: Session = Depends(get_db)):
    appointment = Appointment(
        patient_id=data.patient_id,
        doctor_id=data.doctor_id,
        appointment_date=datetime.utcnow()
    )
    db.add(appointment)
    db.commit()
    return {"message": "Appointment booked"}

@router.get("/")
def get_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()