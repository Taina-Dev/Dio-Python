import datetime

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.saques_realizados = 0
        self.transacoes = []  #Lista para armazenar as transacoes do dia

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((datetime.datetime.now(), f"Depósito de R${valor:.2f}"))
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    
    def sacar(self, valor):
        if self.saldo <= 0:
            print("Não há saldo disponível para saque.")
        elif self.saques_realizados >= 3:
            print("Você atingiu o limite diário de saques.")
        elif valor > 500:
            print("O valor máximo de saque é de R$500.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.transacoes.append((datetime.datetime.now(), f"Saque de R${valor:.2f}"))
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def extrato(self):
        print(f"Extrato do dia: {datetime.datetime.now().date()}")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("Transações do dia:")
        for transacao in self.transacoes:
            print(f"- {transacao[1]} em {transacao[0].strftime('%H:%M:%S')}")

#Para exibir o menu
def menu():
    conta = ContaBancaria()
    while True:
        print("\nMENU:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor_deposito)
        elif opcao == "2":
            valor_saque = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor_saque)
        elif opcao == "3":
            conta.extrato()
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()
