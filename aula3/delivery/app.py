from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, Codeshow</h1>"


@app.route("/sobre")
def sobre():
    return "<p>este é o melhor site de delivery</p>"