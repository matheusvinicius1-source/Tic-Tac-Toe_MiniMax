# ==========================================
# AGENTE
# ==========================================

def criar_agente(simbolo):
    return {
        "simbolo": simbolo
    }


def obter_jogadas_disponiveis(tabuleiro):
    jogadas = []

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                jogadas.append((linha, coluna))

    return jogadas


def fazer_jogada(tabuleiro, jogada, simbolo):
    linha, coluna = jogada

    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = simbolo
        return True

    return False
