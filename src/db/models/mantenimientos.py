from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from src.db.database import Base, TimestampMixin


class Mantenimientos(Base, TimestampMixin):
    __tablename__ = "MANTENIMIENTOS"

    id = Column(Integer, primary_key=True, index=True)
    fecha_desde = Column(Date, nullable=False)
    fecha_hasta = Column(Date, nullable=True)
    precio = Column(Float, nullable=True)
    detalle = Column(String, nullable=False)
    id_auto = Column(
        Integer,
        ForeignKey("AUTOS.id"),
        nullable=False
    )

autos = relationship(
    "Autos",       
    back_populates="mantenimientos",
)  