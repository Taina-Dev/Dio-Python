import os
import shutil
from pathlib import Path

#Desse modelo ele acha o caminho onde criar 
ROOT_PATH = Path(__file__).parent
print(ROOT_PATH.parent)

#Crio uma nova Pasta um diretorio
#os.mkdir(ROOT_PATH / "Banco")
#arquivo = open(ROOT_PATH / "conexao_banco.py", "w")
#arquivo.close()

#Modelo rename de como altera renome um arquivo 
#os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

#Remove um arquivo
#os.remove(ROOT_PATH/ "alterado.txt")

#Move um arquivo
shutil.move(ROOT_PATH/ 'conexao_banco.py', ROOT_PATH / 'Banco' )