from abc import ABC, abstractmethod
import textwrap
from datetime import datetime, timedelta


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta(ABC):
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0007"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor <= 0:
            print("Não há saldo disponível para saque.")
            return False

        if numero_saques >= self.limite_saques:
            print("Você atingiu o limite diário de saques.")
            return False

        if valor > self.limite:
            print("O valor máximo de saque é de R$500.")
            return False

        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False

        self._saldo -= valor
        self.historico.adicionar_transacao(Saque(valor))
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False

        self._saldo += valor
        self.historico.adicionar_transacao(Deposito(valor))
        return True

    def __str__(self):
        return f"""\
          Agencia:\t{self.agencia}
          C/C:\t{self.numero}
          Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.depositar(self.valor)
        conta.historico.adicionar_transacao(self)


def criar_cliente(clientes):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço (logradouro, número, bairro, cidade/estado): ")

   
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf_numeros, endereco=endereco)
    clientes.append(cliente)
    print("Cliente criado com sucesso!!")


def criar_conta(contas, clientes):
    cpf_cliente = input("Digite o CPF do cliente: ")

    for cliente in clientes:
        if cliente.cpf == cpf_cliente:
            numero_conta = len(contas) + 1
            conta = ContaCorrente(numero_conta, cliente)
            contas.append(conta)
            print("Conta criada com sucesso.")
            return

    print("Cliente não encontrado.")


def depositar(contas):
    cpf_cliente = input("Digite o CPF do cliente: ")

    for conta in contas:
        if conta.cliente.cpf == cpf_cliente:
            valor = float(input("Informe o valor do depósito: "))
            if conta.depositar(valor):
                print(f"Depósito de R${valor:.2f} realizado com sucesso.")
                return
            else:
                print("Falha ao realizar o depósito.")
                return

    print("Conta não encontrada.")


def sacar(contas):
    cpf_cliente = input("Digite o CPF do cliente: ")

    for conta in contas:
        if conta.cliente.cpf == cpf_cliente:
            valor = float(input("Digite o valor a ser sacado: "))
            if conta.sacar(valor):
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
                return
            else:
                print("Falha ao realizar o saque.")
                return

    print("Conta não encontrada.")


def extrato_semanal(contas):
    cpf_cliente = input("Digite o CPF do cliente: ")
    inicio_semana = datetime.now().date() - timedelta(days=datetime.now().weekday())
    fim_semana = inicio_semana + timedelta(days=6)

    for conta in contas:
        if conta.cliente.cpf == cpf_cliente:
            print("======= Extrato Semanal =======")
            transacoes = [transacao for transacao in conta.historico.transacoes
                          if inicio_semana <= datetime.strptime(transacao['data'], "%d-%m-%Y %H:%M:%S").date() <= fim_semana]

            if not transacoes:
                print("Nenhuma transação realizada nesta semana.")
            else:
                for transacao in transacoes:
                    print(f"- {transacao['tipo']} - Valor: R${transacao['valor']:.2f} - Data: {transacao['data']}")

            print(f"\nSaldo: R$ {conta.saldo:.2f}")
            print("===============================")
            return

    print("Conta não encontrada.")


def extrato_mensal(contas):
    cpf_cliente = input("Digite o CPF do cliente: ")
    hoje = datetime.now()
    primeiro_dia_mes = datetime(hoje.year, hoje.month, 1)
    ultimo_dia_mes = primeiro_dia_mes.replace(day=28) + timedelta(days=4)

    if ultimo_dia_mes.month != hoje.month:
        ultimo_dia_mes = primeiro_dia_mes.replace(day=1) - timedelta(days=1)

    for conta in contas:
        if conta.cliente.cpf == cpf_cliente:
            print("======= Extrato Mensal =======")
            if not conta.historico.transacoes:
                print("Nenhuma transação realizada nesta conta.")
                print("===============================")
                return

            transacoes = [transacao for transacao in conta.historico.transacoes
                      if primeiro_dia_mes <= datetime.strptime(transacao['data'], "%d-%m-%Y %H:%M:%S") <= ultimo_dia_mes]

            
            if not transacoes:
                print("Nenhuma transação realizada neste mês.")
            else:
                for transacao in transacoes:
                    print(f"- {transacao['tipo']} - Valor: R${transacao['valor']:.2f} - Data: {transacao['data']}")

            print(f"\nSaldo: R$ {conta.saldo:.2f}")
            print("===============================")
            return

    print("Conta não encontrada.")


def extrato(contas):
    while True:
        print("\nExtrato:")
        print("1 - Extrato Diário")
        print("2 - Extrato Semanal")
        print("3 - Extrato Mensal")
        print("4 - Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            extrato_diario(contas)
        elif opcao == "2":
            extrato_semanal(contas)
        elif opcao == "3":
            extrato_mensal(contas)
        elif opcao == "4":
            return
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


def extrato_diario(contas):
    cpf_cliente = input("Digite o CPF do cliente: ")
    hoje = datetime.now().date()

    for conta in contas:
        if conta.cliente.cpf == cpf_cliente:
            print("======= Extrato Diário =======")
            transacoes = [transacao for transacao in conta.historico.transacoes
                          if datetime.strptime(transacao['data'], "%d-%m-%Y %H:%M:%S").date() == hoje]

            if not transacoes:
                print("Nenhuma transação realizada hoje.")
            else:
                for transacao in transacoes:
                    print(f"- {transacao['tipo']} - Valor: R${transacao['valor']:.2f} - Data: {transacao['data']}")

            print(f"\nSaldo: R$ {conta.saldo:.2f}")
            print("===============================")
            return

    print("Conta não encontrada.")


def buscar_conta_bancaria(contas):
    cpf_cliente = input("Digite o CPF do cliente: ")

    for conta in contas:
        if conta.cliente.cpf == cpf_cliente:
            print("Conta encontrada.")
            print(f"Agência: {conta.agencia}")
            print(f"Número da Conta: {conta.numero}")
            print(f"Titular: {conta.cliente.nome}")
            return

    print("Conta não encontrada.")


def localizar_cliente_por_cpf(clientes):
    cpf_cliente = input("Digite o CPF do cliente: ")

    for cliente in clientes:
        if cliente.cpf == cpf_cliente:
            print("Cliente encontrado.")
            print(f"Nome: {cliente.nome}")
            print(f"Data de Nascimento: {cliente.data_nascimento}")
            print(f"Endereço: {cliente.endereco}")
            return

    print("Cliente não encontrado.")


def menu(contas):
    clientes = []
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
            criar_cliente(clientes)
        elif opcao == "2":
            criar_conta(contas, clientes)
        elif opcao == "3":
            depositar(contas)
        elif opcao == "4":
            sacar(contas)
        elif opcao == "5":
            extrato(contas)
        elif opcao == "6":
            buscar_conta_bancaria(contas)
        elif opcao == "7":
            localizar_cliente_por_cpf(clientes)
        elif opcao == "8":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu([])

