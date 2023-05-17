from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from model.Engine import getEngine
from model.model import *

with Session(getEngine()) as session:

    def IngresarPlaca(placa, cedula):
        print(f"registrando Placa {placa} en BD para el usuario {cedula}")

    def buscarPlaca(placa):
        print(placa)
        stmt = select(Vehiculo).where(Vehiculo.placa.in_([placa]))
        result = session.scalars(stmt).first()
        return(result is not None)


    # Manuel = Usuario(
    #     cedula = '123',
    #     nombre = 'Manuel',
    #     celdas = [],
    #     vehiculos = []
    # )

    # Herbbie = Vehiculo(
    #     placa="TAD338",
    #     user_id="123"
    # )

    # session.add(Herbbie)
    # session.commit()

    '''
    try:
        session.add_all([Manuel,zora,durango])
        session.commit()
    except IntegrityError:
        print("error, algun usuario ya existe")
    

    while(True):
        numero = input("Ingrese el numero de la celda")
        userid = input("ingrese cedula propietario")
        
        session.add(Celda(numero=numero,estado=True,user_id=userid))
        session.commit()
    '''
