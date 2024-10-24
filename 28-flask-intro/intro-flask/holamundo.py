import mariadb
from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)


midb = mariadb.connect(
    host='localhost',
    user='root',  # Mejor no usar el usuario root
    password='...',  # Recordar poner el password...
    database='prueba'
)

cursor = midb.cursor(dictionary=True)


@app.route('/')
def index():
    return 'hola mundo'


@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'El método NO ES GET'

# La llamada a curl:
# 	curl -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000/lele


@app.route('/lele', methods=['POST', 'GET'])
def lele():
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    print(usuarios)
    # Llamamos a la función url_for con en nombre de la función a la que vamos
    # print(url_for('index'))
    # Si la función tiene argumentos le pasamos sus valores como argumentos nombrados
    # SIEMPRE ponemos return al redirect para poder ir allá
    # abort(401)
    # return redirect(url_for('lala', post_id=2))
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    # return render_template('lele.html')
    return render_template('lele.html', usuarios=usuarios)


@app.route('/home_simple', methods=['GET'])
def home_simple():
    return render_template('home_simple.html', mensaje='Hola Mundo!')


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola Mundo!')


@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        sql = "insert into usuario (username, email, edad) values (%s, %s, %s)"
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for('lele'))
    return render_template('crear.html')
