from flask import Flask ,render_template,request,Session





app = Flask(__name__)

notes = []


@app.route("/", methods=["GET","POST"])

def index():
    if request.method == "POST":
        note = request.form.get('note')
        notes.append(note)
    return render_template('index.html', noted=notes)


app.run(debug=True)

