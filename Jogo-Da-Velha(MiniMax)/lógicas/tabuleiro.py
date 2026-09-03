def criar_tabuleiro():
    return [" ", " ", " ",
            " ", " ", " ",
            " ", " ", " "]


def mostrar_tabuleiro(tabuleiro):
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("-----------")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("-----------")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
    print()


def movimentos_disponiveis(tabuleiro):
    movimentos = []

    for posicao in range(9):
        if tabuleiro[posicao] == " ":
            movimentos.append(posicao)

    return movimentos


def fazer_jogada(tabuleiro, posicao, jogador):
    if posicao < 0 or posicao > 8:
        return False

    if tabuleiro[posicao] != " ":
        return False

    tabuleiro[posicao] = jogador

    return True


def verificar_vitoria(tabuleiro, jogador):
    vitorias = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for combinacao in vitorias:
        if (
            tabuleiro[combinacao[0]] == jogador
            and tabuleiro[combinacao[1]] == jogador
            and tabuleiro[combinacao[2]] == jogador
        ):
            return True

    return False


def verificar_empate(tabuleiro):
    if len(movimentos_disponiveis(tabuleiro)) == 0:
        if not verificar_vitoria(tabuleiro, "X") and not verificar_vitoria(tabuleiro, "O"):
            return True

    return False

#Esse main é apenas para testar as funções do tabuleiro, não faz parte da lógica do jogo.
if __name__ == "__main__":

    tabuleiro = criar_tabuleiro()

    mostrar_tabuleiro(tabuleiro)

    fazer_jogada(tabuleiro, 0, "X")
    fazer_jogada(tabuleiro, 4, "O")
    fazer_jogada(tabuleiro, 1, "X")
    fazer_jogada(tabuleiro, 5, "O")
    fazer_jogada(tabuleiro, 2, "X")

    mostrar_tabuleiro(tabuleiro)

    print("Movimentos disponiveis:")
    print(movimentos_disponiveis(tabuleiro))

    print("X venceu?")
    print(verificar_vitoria(tabuleiro, "X"))

    print("O venceu?")
    print(verificar_vitoria(tabuleiro, "O"))

    print("Empate?")
    print(verificar_empate(tabuleiro))