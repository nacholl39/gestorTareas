#Importamos las librerias para poder usar sus métodos.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#1. Crear el "Engine", que permite a "sqlarchemy" comunicarse con la base de datos.
engine = create_engine("sqlite:///database/tareas.db", connect_args={'check_same_thread': False})

#2. Creamos la sesión, lo que nos va a permitir realizar las operaciones de nuestra base de datos.
Session = sessionmaker(bind=engine)
session = Session()

#3. Esta vinculación es la que va a transformar las clases en tablas.
#La clase que queramos que se transforme en una tabla, solo tenemos que hacer que herede de la clase "Base" que hemos creado.
Base = declarative_base()