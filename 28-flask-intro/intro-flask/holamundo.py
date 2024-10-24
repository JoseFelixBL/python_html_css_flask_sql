from flask import Flask, request
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


@app.route('/lele')
def lele():
    return 'lele'
