from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'hola mundo'


@app.route('/post/<post_id>')
def lala(post_id):
    return 'El id del post es: ' + post_id


@app.route('/lele')
def lele():
    return 'lele'
