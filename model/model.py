from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "Usuario"
    cedula: Mapped[str] = mapped_column(String(10), primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30))

    celdas: Mapped[List["Celda"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    
    vehiculos: Mapped[List["Vehiculo"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return self.nombre
        #return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Vehiculo(Base):
    __tablename__ = "Vehiculo"
    id: Mapped[int] = mapped_column(primary_key=True)
    placa: Mapped[str] = mapped_column(String(6), unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Usuario.cedula"))
    user: Mapped["Usuario"] = relationship(back_populates="vehiculos")
    def __repr__(self) -> str:
        return self.placa
        #return f"Address(id={self.id!r}, email_address={self.email_address!r})"

class Celda(Base):
    __tablename__ = "Celda"
    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str]
    estado: Mapped[bool]
    user_id: Mapped[int] = mapped_column(ForeignKey("Usuario.cedula"))
    user: Mapped["Usuario"] = relationship(back_populates="celdas")
    def __repr__(self) -> str:
        return self.placa
    
engine = create_engine("sqlite:///db.sqlite", echo=True)
Base.metadata.create_all(engine)


