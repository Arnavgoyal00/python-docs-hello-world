from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "_main_":
    app.run(debug=True)
