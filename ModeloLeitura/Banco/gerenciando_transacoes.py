import sqlite3
from pathlib import Path

ROOTH_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOTH_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
   cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 3", "Teste3@gmail.com"))
   cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2,"Teste 4", "Teste4@gmail.com"))
   conexao.commit()
except Exception as exc:
    print(f"Ops!! um erro ocorreu!!  {exc}")
    conexao.rollback()   

        