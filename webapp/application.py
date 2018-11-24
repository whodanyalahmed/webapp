from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello! world!!!This is dan!"

@app.route("/danyal")
def danyal():
	return "Hello! Danyal"

@app.route("/<string:name>")

def hello(name):
	name = name.capitalize()
	return f"<h1>Hello! {name}</h1>"


app.run() 