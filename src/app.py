from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! v1.0.0.6"
