import mariadb


def select_all():
    cursor.execute('select * from usuario')
    filas_afectadas = cursor.rowcount
    resultado = cursor.fetchall()
    print(resultado)
    print(f'Filas SELECTed {filas_afectadas}')


def select_one():
    cursor.execute('select * from usuario limit 1')
    resultado = cursor.fetchall()
    print(resultado)
    print(f'Filas SELECTed con LIMIT 1: {cursor.rowcount}')


def modelo_db():
    # Para recordar el modelo de la base de datos
    cursor.execute('show create table usuario')
    resultado = cursor.fetchall()

    for dato in resultado:
        for item in list(dato):
            print(item)


def insertar_datos():
    # Para insertar datos
    sql = 'insert into usuario (email, username, edad) values (%s, %s, %s)'
    values = ('micorreo@correo.com', 'nombre usuario', 45)

    cursor.execute(sql, values)

    midb.commit()

    print(f'Filas INSERTADAS: {cursor.rowcount}')


def actualiza_datos():
    sql = 'update usuario set email = %s where id = %s'
    values = ('micorreo@correo.co.nz', 4)
    cursor.execute(sql, values)
    midb.commit()
    print(f'Filas ACTUALIZADAS: {cursor.rowcount}')


def eliminar_datos():
    sql = 'delete from usuario where id = %s'
    values = (4, )
    # Es MUY IMPORTANTE terminar con ", " para indicar que es una TUPLA de un solo elemento
    cursor.execute(sql, values)
    midb.commit()
    print(f'Filas ELIMINADAS: {cursor.rowcount}')


midb = mariadb.connect(
    host='localhost',
    user='root',  # Mejor no usar el usuario root
    password='...',  # Recordar poner el password...
    database='prueba'
)

cursor = midb.cursor()

# select_all()

# modelo_db()

# insertar_datos()
# select_all()

# select_all()
# actualiza_datos()
# select_all()

# eliminar_datos()
# select_all()

select_one()
