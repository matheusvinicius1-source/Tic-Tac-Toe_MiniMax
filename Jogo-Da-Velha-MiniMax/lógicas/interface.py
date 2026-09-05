# Função para exibir as instruções do jogo
def exibir_tabuleiro_instrucoes():

    print("\n--- POSIÇÕES NO TABULEIRO ---")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("-----------------------------\n")

# Função para exibir o tabuleiro atual
def exibir_tabuleiro_atual(tabuleiro):

    print()

    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("-----------")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("-----------")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")

    print()


# Função para obter a jogada do jogador humano
def obter_jogada_humano(tabuleiro):

    while True:

        entrada = input(
            "Escolha uma posição livre (1-9): "
        ).strip()

        if not entrada.isdigit():
            print(
                "Entrada inválida! "
                "Digite apenas números de 1 a 9."
            )
            continue

        posicao = int(entrada) - 1

        if posicao < 0 or posicao > 8:
            print(
                "Posição fora do limite! "
                "Escolha um número entre 1 e 9."
            )
            continue

        if tabuleiro[posicao] != " ":
            print(
                "Essa posição já está ocupada! "
                "Escolha outra."
            )
            continue

        return posicao

#Menu inicial do jogo
def menu_inicial():
    print("========================================")
    print("    JOGO DA VELHA — HUMANO VS AGENTE    ")
    print("========================================")
    print("1. Jogar como X (Você começa)")
    print("2. Jogar como O (O Agente começa)")

    while True:

        opcao = input(
            "Escolha a opção (1 ou 2): "
        ).strip()

        if opcao == "1":
            return "X", "O"

        if opcao == "2":
            return "O", "X"

        print(
            "Opção inválida! "
            "Escolha 1 ou 2."
        )
