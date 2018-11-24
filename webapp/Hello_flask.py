from flask import Flask
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello World all the way from \nFlask'

@app.route('/searchl')
def do_search() -> str:
    return str(search4letters('Danyal','aeiou'))

@app.route('/add')
def add():
    return 5+5


app.run()

