from flask import Flask, render_template
app = Flask(__name__)
#in the function return render_template(‘index.html’)
@app.route("/Flask")
def student_webpage():
    name='John'
    return render_template('Me.html',student_name = name)

app.run(debug=True)
