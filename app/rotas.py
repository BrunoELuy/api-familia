from flask import request, Response, jsonify
import json
from db import get_familia, get_familiar, post_update_familiar, post_new_familiar, del_familiar, patch_familiar


def registrar_rotas(app):

    @app.route('/familia', methods=['GET'])
    def listar_familia():
        dados = get_familia()
        return Response(
            json.dumps(dados, ensure_ascii=False),
            content_type='application/json'
        )

    @app.route('/familia/<int:id>', methods=['GET'])
    def obter_familiar(id):
        dado = get_familiar(id)

        # Verifica se retornou erro
        if isinstance(dado, tuple):  # Ex: ({"erro": "..."}, 404)
            return Response(
                json.dumps(dado[0], ensure_ascii=False),
                content_type='application/json'
            ), dado[1]

        return Response(
            json.dumps(dado, ensure_ascii=False),
            content_type='application/json'
        )

    @app.route('/familia/<int:id>', methods=['POST'])
    def update_familiar(id):
        dados = request.get_json()
        resultado = post_update_familiar(id, dados)

        return Response(
            json.dumps(resultado, ensure_ascii=False),
            content_type='application/json'
        )
    
    @app.route('/familia/<int:id>', methods=['DELETE'])
    def deletar_familiar(id):
        return jsonify(del_familiar(id))
    
    @app.route('/familia/<int:id>', methods=['PATCH'])
    def atualizar_parcial_familiar(id):
        dados = request.get_json()
        return jsonify(patch_familiar(id, dados))

    @app.route('/familia/new', methods=['POST'])
    def new_familiar():
        dados = request.get_json()
        resultado = post_new_familiar(dados)

        return Response(
            json.dumps(resultado, ensure_ascii=False),
            content_type='application/json'
        )
