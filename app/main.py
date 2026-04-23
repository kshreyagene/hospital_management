from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, patient, doctor, appointment

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hospital Management API")

app.include_router(auth.router)
app.include_router(patient.router)
app.include_router(doctor.router)
app.include_router(appointment.router)