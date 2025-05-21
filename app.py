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


@app.route('/familia', methods=['GET'])
def listar_familia():
    return jsonify(get_familia())


if __name__ == "__main__":
    app.run(debug=True)
