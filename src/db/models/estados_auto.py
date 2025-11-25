from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db.database import Base, TimestampMixin


class EstadosAuto(Base, TimestampMixin):
    __tablename__ = "ESTADOS_AUTO"

    id = Column(Integer, primary_key=True, index=True)
    estado = Column(String, nullable=False) 

alquileres = relationship(
    "Autos",       
    back_populates="estados_auto",
)