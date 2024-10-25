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
            database=current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)

    db.commit()


# Si escribo flask init_db se llamará a esta función
# with_appcontext es Para que pueda acceder a las variables de contexto DATABASE_HOST...
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')


def init_app(app):
    # Le indica a flask que tiene que cerra la conexión a DB cuando termine una petición
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
