import sqlite3

def conectar():
    return sqlite3.connect("familia.db")

def get_familia():
    con = conectar()
    cur = con.cursor()
    cur.execute(
        "SELECT nome, idade, parentesco, hobbies, emprego FROM familiares"
        )
    dados = cur.fetchall()
    con.close()

    lista = [{"nome": nome, "idade": idade, "parentesco": parentesco, "hobbies": hobbies,
              "emprego": emprego} for nome, idade, parentesco, hobbies, emprego in dados]
    return lista

def get_familiar(id):
    con = conectar()
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
    return {"erro": "Familiar não encontrado"}, 404

def post_update_familiar(id, dados):
    con = conectar()
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
    """,(
        dados.get('nome'),
        dados.get('idade'),
        dados.get('parentesco'),
        dados.get('hobbies'),
        dados.get('emprego'),
        id
    ))

    con.commit()
    con.close()
    return {"mensagem": f"Familiar com id {id} atualizado com sucesso!"}