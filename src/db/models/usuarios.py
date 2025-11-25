from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from src.db.database import Base, TimestampMixin


class Usuarios(Base, TimestampMixin):
    __tablename__ = "USUARIOS"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    contraseña = Column(String, nullable=True, unique=True)
    email = Column(String, nullable=False) 
    dni = Column(String, nullable=False, unique=True)
    telefono = Column(String, nullable=True)
    carnet_conducir = Column(Boolean, nullable=False, default=False)
    id_rol = Column(
        Integer,             
        ForeignKey("ROLES_USUARIOS.id"),
        nullable=True)
         
  
    alquileres = relationship( 
        "Alquileres",
        back_populates="usuarios",
    )

    usuarios_roles = relationship(
        "RolesUsuarios",
        back_populates="usuarios",
    )