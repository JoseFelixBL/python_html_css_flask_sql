from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)


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
    return {
        "username": "Chanchito Feliz",
        "email": "chanchito@feliz.com"
    }
