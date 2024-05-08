import random

def jogar_jokenpo():
    print("Bem-vindo ao Jogo Pedra, Papel e Tesoura!\n")
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

    opcoes = ['Pedra', 'Papel', 'Tesoura']
    jogador = int(input("Digite sua escolha (1, 2 ou 3): ")) - 1

    if jogador < 0 or jogador > 2:
        print("Escolha inválida. Por favor, escolha entre 1, 2 ou 3.")
        return

    escolha_jogador = opcoes[jogador]
    escolha_computador = random.choice(opcoes)

    print(f"Você escolheu: {escolha_jogador}")
    print(f"O computador escolheu: {escolha_computador}")

    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif (escolha_jogador == "Pedra" and escolha_computador == "Tesoura") or \
         (escolha_jogador == "Papel" and escolha_computador == "Pedra") or \
         (escolha_jogador == "Tesoura" and escolha_computador == "Papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

# Função principal para iniciar o jogo
def main():
    jogar_novamente = True
    while jogar_novamente:
        jogar_jokenpo()
        resposta = input("Deseja jogar novamente? (s/n): ")
        if resposta.lower() != 's':
            jogar_novamente = False
            print("Obrigado por jogar!")

# Iniciar o jogo
if __name__ == "__main__":
    main()