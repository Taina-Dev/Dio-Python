
# Para ler um arquivo
file = open('example.txt', 'r')
print(file.read())
file.close()

# Para escrever um arquivo
file = open('example.txt', 'w')
print(file.readline())
file.close()

# Para anexar conteúdo a  um arquivo existente
file = open('example.txt', 'a')
print(file.read())
file.close()