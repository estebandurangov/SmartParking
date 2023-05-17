from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from database.Engine import getEngine
from database.model import *

#from Engine import getEngine
#from model import *

with Session(getEngine()) as session:

    def IngresarPlaca(placa, cedula):
        print(f"registrando Placa {placa} en BD para el usuario {cedula}")

    def buscarPlaca(placa):
        stmt = select(Vehiculo).where(Vehiculo.placa.in_([placa]))
        result = session.scalars(stmt).first()
        return result is not None

    '''
    Manuel = Vehiculo(
         placa = 'TAD338',
         user_id = '123',
    )

    session.add(Manuel)
    session.commit()
    '''
