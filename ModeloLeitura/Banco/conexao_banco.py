import sqlite3
from pathlib import Path

ROOTH_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOTH_PATH / "meu_banco.db")
cursor = conexao.cursor()

def criar_tabela(cursor):
  cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")


def inserir_registro(conexao, cursor, nome , email):
 data = (nome, email)
 cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", data)
 conexao.commit()


def atualizar_registros(conexao, cursor, nome , email, id):
 data = (nome, email, id)
 cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
 conexao.commit()

#atualizar_registros(conexao, cursor, "DIO.ME", "dio.me@gamil.com", 1)


def deletar_registros(conexao, cursor, id):
 data = (id,)
 cursor.execute("DELETE FROM clientes WHERE id=?;", data)
 conexao.commit()

deletar_registros(conexao, cursor, 11, 12, 13, 14)

def inserir_muitos(conexao, cursor, dados):
   cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
   conexao.commit()

dados = [
  ("Taina", "Dio.me@gamil.com"),
  ("Lais", "Dio.me@gamil.com"),
  ("Henry", "Dio.me@gamil.com"),
  ("Maria", "Dio.me@gamil.com"),
  ("Isabelly", "Dio.me@gamil.com"),
  ("Alexandre", "Dio.me@gamil.com"),
]   
#inserir_muitos(conexao, cursor, dados)


def recuperar_clientes(cursor, id):
  cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
  return cursor.fetchone()

""" cliente = recuperar_clientes(cursor, 4)
print(cliente) """


def listar_clientes(cursor):
   return cursor.execute("SELECT * FROM clientes ORDER BY nome;")

""" clientes = listar_clientes(cursor)
for cliente in clientes:
   print(cliente) """
   
""" id_cliente = input("Informe o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")
clientes = cursor.fetchall()

for cliente in clientes:
  print(cliente)
 """

""" id_cliente = input("Informe o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id=?", (id_cliente,))
clientes = cursor.fetchall()

for cliente in clientes:
print(cliente)   """