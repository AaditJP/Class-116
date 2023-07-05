from flask import Flask , render_template
app = Flask(__name__)

@app.route("/Activity1")
def student_page():
    name = "Aadit"

    return render_template('index.html',student_name = name )
app.run(debug=True)