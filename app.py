from flask import Flask, jsonify
import sqlite3


app = Flask(__name__)


def get_familia():
    con = sqlite3.connect("familia.db")
    cur = con.cursor()
    cur.execute(
        "SELECT nome, idade, parentesco, hobbies, emprego FROM familiares")
    dados = cur.fetchall()
    con.close()

    lista = [{"nome": nome, "idade": idade, "parentesco": parentesco, "hobbies": hobbies,
              "emprego": emprego} for nome, idade, parentesco, hobbies, emprego in dados]
    return lista


def get_familiar(id):
    con = sqlite3.connect("familia.db")
    cur = con.cursor()
    cur.execute(
        "SELECT id, nome, idade, parentesco, hobbies, emprego FROM familiares WHERE id = ?", (
            id,)
    )
    dado = cur.fetchone()
    con.close()

    if dado:
        familiar = {
            "id": dado[0],
            "nome": dado[1],
            "idade": dado[2],
            "parentesco": dado[3],
            "hobbies": dado[4],
            "emprego": dado[5]
        }
        return familiar
    else:
        return {"erro": "Familiar não encontrado"}, 404


@app.route('/familia/<int:id>', methods=['GET'])
def obter_familiar(id):
    return jsonify(get_familiar(id))


@app.route('/familia', methods=['GET'])
def listar_familia():
    return jsonify(get_familia())


if __name__ == "__main__":
    app.run(debug=True)
