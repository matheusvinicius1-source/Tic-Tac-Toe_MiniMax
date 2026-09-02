def criar_tabuleiro():
    return ([
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ])

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def movimentos_disponiveis(tabuleiro):
    movimentos = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                movimentos.append((i, j))
    return movimentos

tabuleiro = criar_tabuleiro()
tabuleiro[0][0] = "X"
tabuleiro[0][1] = "X"
tabuleiro[0][2] = "X"
imprimir_tabuleiro(tabuleiro)