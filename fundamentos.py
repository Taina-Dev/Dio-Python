""" import time

mensagem = "Vai ser emocionante essa trilha em Python Com a DIO.me  Tainá Correa ;)"


def limpar_tela():
    print("\033[H\033[J", end='')


def exibir_animacao(mensagem):
    for i in range(len(mensagem)):
        limpar_tela()
        print(mensagem[:i+1])
        time.sleep(0.1)  


exibir_animacao(mensagem)


produto_1 = 10
 """

""" saldo = 1000
limete = 500
print(saldo is limete)
print(saldo is not limete) """

""" curso = "Curso Python"
frutas = ["laranja", "uva", "limao"]
saques = [1500,500]
"Pyton"

print("uva" in frutas)
print ("mamao" not in frutas)
print("Python" in curso)
saldo = 500                                                               
saldo += 300   """

""" def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("Retire o seu dinehrio na boca do caixa.")


    print("Obrigado por ser nosso cliente, Bom diaa!")


def depositar(valor):
     saldo = 500
     saldo == valor  
   


sacar(1000)    """     
       
""" saldo = 2000.0
saque = float(input("Informe o valor do saque: "))
Disponivel_Na_Conta = saldo - saque

if saldo >= saque:
    print("Realizado saque!","Saldo Diponivel em conta: ", Disponivel_Na_Conta)
if saldo <= saque:
    print("Saldo insuficiente!" ,saldo)
 """
""" curso = "  taina "
print(curso.upper())
print(curso.strip())
print(curso.title())
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())
print(curso.center(10, "#"))
print(".".join(curso)) """
""" nome = "Tainá"
idade = 28
profissao = "Programador"
linguagem = "Python"
print("Ola, me chama %s. Tenho %d anos de idade , trabalho como %s e estou aprendendo uma loguamgem nova a de %s." % (nome, idade, profissao, linguagem))
print(f"Ola, me chama {nome}. Tenho {idade} anos de idade , trabalho como {profissao} e estou aprendendo uma loguamgem nova a de {linguagem}.") """

""" curso = "  taina "
print(curso.strip())
curso = "Python"                                                     
print(curso[::-1])  """

set([1,1,2,33,4,5,4,4])