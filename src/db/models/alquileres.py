from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from src.db.database import Base, TimestampMixin


class Alquileres(Base, TimestampMixin):
    __tablename__ = "ALQUILERES"

    id = Column(Integer, primary_key=True, index=True)
    fecha_desde = Column(Date, nullable=False)
    fecha_hasta = Column(Date, nullable=False)
    fecha_entrega = Column(Date, nullable=False)
    fecha_devolucion = Column(Date, nullable=True)
    monto_acordado = Column(Float, nullable=False)
    monto_total = Column(Float, nullable=True)
    id_estado_alquiler = Column(
        Integer, 
        ForeignKey("ESTADOS_ALQUILER.id"), 
        nullable=False 
    ) 
    id_usuario = Column(
        Integer, 
        ForeignKey("USUARIOS.id"), 
        nullable=False
    )
    id_auto = Column(
        Integer, 
        ForeignKey("AUTOS.id"), 
        nullable=False
    )

    usuarios = relationship(
        "Usuarios",
        back_populates="alquileres",
    )

    pagos = relationship(
        "Pagos",
        back_populates="alquileres",
    )

    estado_alquiler = relationship(
        "EstadosAlquiler",
        back_populates="alquileres",
    ) 

    autos  = relationship(
        "Autos",
        back_populates="alquileres",
    )     



