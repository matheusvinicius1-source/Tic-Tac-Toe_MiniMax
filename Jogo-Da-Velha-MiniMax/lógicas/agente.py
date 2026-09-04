# ==========================================
# AGENTE MINIMAX
# ==========================================

def minimax(tabuleiro, jogador):
    vencedor = verificar_vencedor(tabuleiro)

    # Vitória do agente
    if vencedor == "O":
        return 1

    # Vitória do jogador
    if vencedor == "X":
        return -1

    # Empate
    if tabuleiro_cheio(tabuleiro):
        return 0

    # ==========================
    # MAX - AGENTE
    # ==========================
    if jogador == "O":

        melhor_valor = -float("inf")

        for linha in range(3):
            for coluna in range(3):

                if tabuleiro[linha][coluna] == " ":

                    # Faz uma jogada do agente
                    tabuleiro[linha][coluna] = "O"

                    # Analisa a resposta do adversário
                    valor = minimax(tabuleiro, "X")

                    # Desfaz a jogada
                    tabuleiro[linha][coluna] = " "

                    melhor_valor = max(melhor_valor, valor)

        return melhor_valor

    # ==========================
    # MIN - ADVERSÁRIO
    # ==========================
    else:

        pior_valor = float("inf")

        for linha in range(3):
            for coluna in range(3):

                if tabuleiro[linha][coluna] == " ":

                    # Faz uma jogada do adversário
                    tabuleiro[linha][coluna] = "X"

                    # Analisa a resposta do agente
                    valor = minimax(tabuleiro, "O")

                    # Desfaz a jogada
                    tabuleiro[linha][coluna] = " "

                    pior_valor = min(pior_valor, valor)

        return pior_valor


# ==========================================
# AGENTE - ESCOLHE A MELHOR JOGADA
# ==========================================

def agente_minimax(tabuleiro):

    melhor_valor = -float("inf")
    melhor_jogada = None

    # Testa todas as posições disponíveis
    for linha in range(3):
        for coluna in range(3):

            if tabuleiro[linha][coluna] == " ":

                # Simula a jogada do agente
                tabuleiro[linha][coluna] = "O"

                # MINIMAX avalia essa jogada
                valor = minimax(tabuleiro, "X")

                # Desfaz a simulação
                tabuleiro[linha][coluna] = " "

                # Guarda a melhor opção
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = (linha, coluna)

    return melhor_jogada
