from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base, TimestampMixin


class Direccion(Base, TimestampMixin):
    __tablename__ = "ESTADO_ALQUILER"

    id = Column(Integer, primary_key=True, index=True)
    estado = Column(String, nullable=False) 

alquileres = relationship(
    "Alquileres",       
    back_populates="estado_alquiler",
)