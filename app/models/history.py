from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    diagnosis = Column(String)
    treatment = Column(String)