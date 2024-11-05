from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, UABC 2024!</p>"

@app.route("/saludo")
def saludoatodos():
    return "<center>Saludos a todos  los que me lean</center>"

@app.route("/about")
def sobremi():
    return "<marquee><h1> Pako@uabc.edu.mx </h1></marquee>"