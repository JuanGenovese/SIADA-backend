from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base, TimestampMixin


class Direccion(Base, TimestampMixin): 
    __tablename__ = "ROLES_USUARIOS"

    id = Column(Integer, primary_key=True, index=True)
    rol = Column(String, nullable=False) 

usuarios = relationship(
    "Usuarios",       
    back_populates="roles_usuarios",
)