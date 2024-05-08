
# Para ler todo um arquivo read para ler aquivos em Python
arquivo = open("ModeloLeitura\lorem.txt", "r")
print(arquivo.read())
arquivo.close() 

# Para ler um arquivo readline para ler linha a linha 
arquivo = open("ModeloLeitura\lorem.txt", "r")
print(arquivo.readline())
arquivo.close()

# Para ler conteúdo a  todo linha a linha porem separa em uma lista 
arquivo = open("ModeloLeitura\lorem.txt", "r")
print(arquivo.readlines())
arquivo.close() 