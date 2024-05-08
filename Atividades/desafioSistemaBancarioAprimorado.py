import datetime

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.saques_realizados = 0
        self.transacoes = []

def depositar(saldo, valor, extrato):
    saldo += valor
    extrato.append((datetime.datetime.now(), f"Depósito de R${valor:.2f}"))
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques):
    if saldo <= 0:
        print("Não há saldo disponível para saque.")
    elif numero_saques >= 3:
        print("Você atingiu o limite diário de saques.")
    elif valor > 500:
        print("O valor máximo de saque é de R$500.")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato.append((datetime.datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    return saldo, extrato, numero_saques

def extrato(saldo, *, extrato):
    print(f"Saldo atual: R${saldo:.2f}")
    print("Transações do dia:")
    for transacao in extrato:
        print(f"- {transacao[1]} em {transacao[0].strftime('%H:%M:%S')}")

def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço (logradouro, número, bairro, cidade/estado): ")
    #Verifica se o CPF já esta cadastrado
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("CPF já cadastrado.")
            return None
    #Extrai apenas os numeros do CPF
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    usuario = Usuario(nome, data_nascimento, cpf_numeros, endereco)
    usuarios.append(usuario)
    return usuario

def criar_conta(contas, usuarios):
    agencia = "0001"
    numero_conta = len(contas) + 1
    print("Selecione um usuário para vincular à conta:")
    cpf_usuario = input("Digite o CPF do usuário: ")
    #Encontra o usuario com o CPF informado
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.cpf == cpf_usuario:
            usuario_encontrado = usuario
            break
    if usuario_encontrado:
        conta = ContaBancaria(agencia, numero_conta, usuario_encontrado)
        contas.append(conta)
        print("Conta criada com sucesso.")
    else:
        print("Usuário não encontrado.")
#Crie a Funcao Localizar conta bancaria
def buscar_conta_bancaria(contas):
    numero_conta = int(input("Digite o número da conta: "))
    for conta in contas:
        if conta.numero_conta == numero_conta:
            print("Conta encontrada.")
            print(f"Agência: {conta.agencia}")
            print(f"Número da Conta: {conta.numero_conta}")
            print(f"Usuário: {conta.usuario.nome}")
            return
    print("Conta não encontrada.")
#Crie a Funcao Localizar cliente pelo Cpf 
def localizar_cliente_por_cpf(usuarios):
    cpf = input("Digite o CPF do cliente: ")
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Cliente encontrado.")
            print(f"Nome: {usuario.nome}")
            print(f"Data de Nascimento: {usuario.data_nascimento}")
            print(f"Endereço: {usuario.endereco}")
            return
    print("Cliente não encontrado.")

def menu(contas):
    usuarios = []
    while True:
        print("\nMENU:")
        print("1 - Criar Usuário")
        print("2 - Criar Conta Bancária")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Extrato")
        print("6 - Buscar Conta Bancária")
        print("7 - Buscar Cliente")
        print("8 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = criar_usuario(usuarios)
            if usuario:
                print("Usuário cadastrado com sucesso.")
        elif opcao == "2":
            criar_conta(contas, usuarios)
        elif opcao == "3":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a ser depositado: "))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    conta.saldo, conta.transacoes = depositar(conta.saldo, valor, conta.transacoes)
                    print(f"Depósito de R${valor:.2f} realizado com sucesso.")
                    break
            else:
                print("Conta não encontrada.")
        elif opcao == "4":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor a ser sacado: "))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    conta.saldo, conta.transacoes, conta.saques_realizados = sacar(conta.saldo, valor, conta.transacoes, 0, conta.saques_realizados)
                    break
            else:
                print("Conta não encontrada.")
        elif opcao == "5":
            numero_conta = int(input("Digite o número da conta: "))
            for conta in contas:
                if conta.numero_conta == numero_conta:
                    extrato(conta.saldo, extrato=conta.transacoes)
                    break
            else:
                print("Conta não encontrada.")
        elif opcao == "6":
            buscar_conta_bancaria(contas)
        elif opcao == "7":
            localizar_cliente_por_cpf(usuarios)
        elif opcao == "8":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu([])
