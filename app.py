from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "esta es mi pagina web cruz pereida ian yahel"
