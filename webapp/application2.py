from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    headline = "Hello!"
    return render_template("hello.html", headliness=headline)

@app.route('/bye')
def bye():
   headline = "Good bye!"
   return render_template("hello.html", headliness=headline)



app.run(debug=True)