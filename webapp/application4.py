from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    names = ['Dan' ,'Casey', 'Soul','Iqu' ]
    return render_template('name.html',names=names)
    
app.run()