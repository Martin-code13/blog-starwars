import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    usuario_id = Column (Integer)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)



    class Favoritos(Base):
        __tablename__ = 'favoritos'
        id = Column(Integer, primary_key=True)
        usuario_id = Column(Integer, ForeignKey('usuario.id'))
        planetas_id = Column(Integer, ForeignKey('planetas.id'))
        vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))
        personajes_id = Column(Integer, ForeignKey('personajes.id'))
       





    class Planetas(Base):
       __tablename__ = 'planetas'
       id = Column(Integer, primary_key=True)
       name = Column(String(250))
       climate = Column(String(250))
       terrain = Column(String(250))


    class Vehiculos(Base):
       __tablename__ = 'vehiculos'
       id = Column(Integer, primary_key=True)
       name = Column(String(250))
       model = Column(String(250))
       manufacturer = Column(String(250))


    class Personajes(Base):
        __tablename__ = 'personajes'
        id = Column(Integer, primary_key=True)
        name = Column(String(250))
        skin_color = Column(String(250))
        gender = Column(String(250))












# class Address(Base):
#     __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    # id = Column(Integer, primary_key=True)
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
