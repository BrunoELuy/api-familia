import sqlite3
from collections import OrderedDict

def conectar():
    return sqlite3.connect("familia.db")

def formatar_familia(dado):
    id, nome, idade, parentesco, hobbies, emprego = dado
    return OrderedDict([
        ("id", id),
        ("nome", nome),
        ("idade", idade),
        ("parentesco", parentesco),
        ("hobbies", hobbies),
        ("emprego", emprego)
    ])

    

def get_familia():
    with conectar() as con:
        cur = con.cursor()
        cur.execute(
            "SELECT id, nome, idade, parentesco, hobbies, emprego FROM familiares"
        )
        dados = cur.fetchall()

        lista = [formatar_familia(dado) for dado in dados]
        return lista


def get_familiar(id):
    with conectar() as con:
        cur = con.cursor()
        cur.execute(
            "SELECT id, nome, idade, parentesco, hobbies, emprego FROM familiares WHERE id = ?", (id,)
        )
        dado = cur.fetchone()
        
        if dado:
            return formatar_familia(dado)

    return {"erro": "Familiar não encontrado"}, 404


def post_update_familiar(id, dados):
    with conectar() as con:
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM familiares WHERE id = ?", (id,)
        )
        existente = cur.fetchone()

        if existente is None:
            cur.close()
            return {"erro": "Familiar não encontrado para atualizar informações"}

        cur.execute("""
            UPDATE familiares
            SET nome = ?, idade = ?, parentesco = ?, hobbies = ?, emprego = ?
            WHERE id = ?
        """, (
            dados.get('nome'),
            dados.get('idade'),
            dados.get('parentesco'),
            dados.get('hobbies'),
            dados.get('emprego'),
            id
        ))

        con.commit()
        cur.close()

    return {"mensagem": f"Familiar com id {id} atualizado com sucesso!"}


def post_new_familiar(dados):
    with conectar() as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO familiares (nome, idade, parentesco, hobbies, emprego)
            VALUES (?, ?, ?, ?, ?)
            """, (
            dados.get('nome'),
            dados.get('idade'),
            dados.get('parentesco'),
            dados.get('hobbies'),
            dados.get('emprego')
        ))

        con.commit()
    return {"mensagem": "Familiar criado com sucesso!"}
