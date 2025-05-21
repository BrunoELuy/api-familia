from flask import jsonify, request
from db import get_familia, get_familiar, post_update_familiar


def registrar_rotas(app):

    @app.route('/familia', methods=['GET'])
    def listar_familia():
        return jsonify(get_familia())

    @app.route('/familia/<int:id>', methods=['GET'])
    def obter_familiar(id):
        return jsonify(get_familiar(id))

    @app.route('/familia/<int:id>', methods=['POST'])
    def update_familiar(id):
        dados = request.get_json()
        return jsonify(post_update_familiar(id, dados))
