import sqlite3

conexao = sqlite3.connect("familia.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS familiares(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER,
               parentesco TEXT,
               hobbies TEXT,
               emprego TEXT
               )
               """)

familia = [
    ("Bruno Eduardo Luy", 19, "Filho mais novo",
     "Programar, jogar basquete, videogames, academia", "Estagiário de Tecnologia da Informação"),
    ("Bernardo Elias Luy", 25, "Filho mais velho", "Programar, acompanhar basquete, investir, treinar",
     "Supervisor de Processos de Segurança da Engenharia"),
    ("Leandro Elias Luy", 53, "Pai",
     "Analisar problemas, acompanhar séries, treinar", "Supervisor de Vendas"),
    ("Marli Terezinha Raimann Luy", 55, "Mãe",
     "Cozinhar, correr, treinar, estudar inglês, meditar", "Dona de casa")
]

cursor.executemany(
    "INSERT INTO familiares (nome, idade, parentesco, hobbies, emprego) VALUES (?, ?, ?, ?, ?)", familia)

conexao.commit()
conexao.close()

print("Banco criado com sucesso")
