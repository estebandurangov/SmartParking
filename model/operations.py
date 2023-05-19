
from sqlalchemy.orm import Session
from  sqlalchemy.exc import IntegrityError
from model import *

with Session(engine) as session:

    def IngresarPlaca(placa, cedula):
        print(f"registrando Placa {placa} en BD para el usuario {cedula}")

    Manuel = Usuario(
        cedula = '123',
        nombre = 'Manuel',
        celdas = [],
        vehiculos = []
    )

    zora = Usuario(
        cedula = '123456',
        nombre = 'Felipe',
        celdas = [],
        vehiculos = []
    )

    durango = Usuario(
        cedula = '789',
        nombre = 'durango',
        celdas = [],
        vehiculos = []
    )
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
