import mariadb

import click
# Para poder ejecutar comandos en la terminal y crear tablas sin ir a Workbench
from flask import current_app, g
# current_app   Mantiene la app que estamos ejecutando
# g es una variable que se enccuentra en toda nuiestra aplicación, lo usaremos para almacenar el usuario dentro de g
from flask.cli import with_appcontext
# cuando ejecutemos el script de DDBB, vamos a necesitar el contexto de la config de nuestra app
from .schema import instructions
# el arch. schema tiene todos los scripts para crear nuestra DDBB


def get_db():
    if 'db' not in g:
        g.db = mariadb.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE'],
        )
