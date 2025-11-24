from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base, TimestampMixin


class Direccion(Base, TimestampMixin):
    __tablename__ = "AUTOS" 

    id = Column(Integer, primary_key=True, index=True)
    fecha_alta = Column(String, nullable=True)
    fecha_baja = Column(String, nullable=True)
    precio_diario = Column(String, nullable=True)
    marca = Column(Integer, nullable=False)
    modelo = Column(Integer, nullable=False)
    anio = Column(Integer, nullable=False)
    patente = Column(Integer, nullable= True, unique=True)
    kilometros = Column(Integer, nullable=False)
    id_estado_auto = Column(
        Integer, 
        ForeignKey("ESTADOS_AUTO.id"), 
        nullable=False
    ) 

    alquileres = relationship(
        "Alquileres",
        back_populates="autos",
    )

    mantenimientos = relationship(
        "Mantenimientos",
        back_populates="autos",
    )

    estadosAuto = relationship(
        "EstadosAutos",
        back_populates="autos",
    )