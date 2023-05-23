from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from database.Engine import getEngine
from database.model import *

with Session(getEngine()) as session:

    def createVehicle(newPlate, newUserId):
        newVehicle = Vehiculo(
            placa = newPlate,
            user_id = newUserId
        )
        session.add(newVehicle)
        session.commit()
        print(f"Registrado Placa {newPlate} en BD para el usuario {newUserId}")

    def readPlate(placa):
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
