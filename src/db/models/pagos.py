from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from src.db.database import Base, TimestampMixin


class Pagos(Base, TimestampMixin):
    __tablename__ = "PAGOS"

    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float, nullable=False)
    fecha = Column(DateTime, nullable=False)
    metodo = Column(String, nullable=False) 
    id_alquiler = Column(
        Integer, 
        ForeignKey("ALQUILERES.id"), 
        nullable=False
    )

alquileres = relationship(
    "Alquileres",       
    back_populates="pagos",
)