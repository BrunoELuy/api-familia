from flask import Flask
from rotas import registrar_rotas

app = Flask(__name__)
registrar_rotas(app)

if __name__ == "__main__":
    app.run(debug=True)
