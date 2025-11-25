from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db.database import Base, TimestampMixin


class EstadosAlquiler(Base, TimestampMixin):
    __tablename__ = "ESTADOS_ALQUILER"

    id = Column(Integer, primary_key=True, index=True)
    estado = Column(String, nullable=False) 

alquileres = relationship(
    "Alquileres",       
    back_populates="estados_alquiler",
)