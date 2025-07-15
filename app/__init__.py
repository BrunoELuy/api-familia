from flask import Flask
from .rotas import registrar_rotas

def create_app():
    app = Flask(__name__)
    registrar_rotas(app)
    return app
