#Implementação do algoritmo Minimax com poda Alfa-Beta
#para o Jogo da Velha.

#O tabuleiro é representado por uma lista de 9 posições:
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

from typing import Optional

try:
    from .tabuleiro import movimentos_disponiveis
except ImportError:
    from tabuleiro import movimentos_disponiveis


VAZIO = " "


def verificar_vencedor(tabuleiro):
    
    # Verifica se X ou O venceu.
    # Retorna:
    # "X"       -> X venceu
    # "O"       -> O venceu
    # "Empate"  -> tabuleiro cheio sem vencedor
    # None      -> jogo ainda em andamento

    vitorias = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),

        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in vitorias:

        if (
            tabuleiro[a] != VAZIO
            and tabuleiro[a] == tabuleiro[b]
            and tabuleiro[a] == tabuleiro[c]
        ):
            return tabuleiro[a]

    if not movimentos_disponiveis(tabuleiro):
        return "Empate"

    return None


def minimax(
    tabuleiro,
    profundidade,
    alfa,
    beta,
    maximizando,
    jogador_agente,
    jogador_humano
):

    #Executa o algoritmo Minimax com poda Alfa-Beta. 
    #O agente é o jogador MAX. 
    #O humano é o jogador MIN.
    
    #Pontuação: 
    #vitória do agente  -> 10 - profundidade
    #vitória humana -> profundidade - 10
    #empate -> 0

    resultado = verificar_vencedor(tabuleiro)

    # Estado terminal: agente venceu
    if resultado == jogador_agente:
        return 10 - profundidade

    # Estado terminal: humano venceu
    if resultado == jogador_humano:
        return profundidade - 10

    # Estado terminal: empate
    if resultado == "Empate":
        return 0


    # MAX — vez do agente
    if maximizando:

        melhor_valor = float("-inf")

        for posicao in movimentos_disponiveis(tabuleiro):

            # Faz a jogada do agente
            tabuleiro[posicao] = jogador_agente

            valor = minimax(
                tabuleiro,
                profundidade + 1,
                alfa,
                beta,
                False,
                jogador_agente,
                jogador_humano
            )

            # Desfaz a jogada
            tabuleiro[posicao] = VAZIO

            melhor_valor = max(melhor_valor, valor)

            # Atualiza Alfa
            alfa = max(alfa, melhor_valor)

            # Poda Alfa-Beta
            if beta <= alfa:
                break

        return melhor_valor


    # MIN — vez do humano
    else:

        pior_valor = float("inf")

        for posicao in movimentos_disponiveis(tabuleiro):

            # Faz a jogada do humano
            tabuleiro[posicao] = jogador_humano

            valor = minimax(
                tabuleiro,
                profundidade + 1,
                alfa,
                beta,
                True,
                jogador_agente,
                jogador_humano
            )

            # Desfaz a jogada
            tabuleiro[posicao] = VAZIO

            pior_valor = min(pior_valor, valor)

            # Atualiza Beta
            beta = min(beta, pior_valor)

            # Poda Alfa-Beta
            if beta <= alfa:
                break

        return pior_valor


def melhor_jogada(
    tabuleiro,
    jogador_agente="O",
    jogador_humano="X"
):
    #Procura a melhor jogada possível para o agente e Retorna um número entre 0 e 8.

    melhor_valor = float("-inf")
    melhor_posicao = None

    alfa = float("-inf")
    beta = float("inf")

    for posicao in movimentos_disponiveis(tabuleiro):

        # Testa a jogada
        tabuleiro[posicao] = jogador_agente

        valor = minimax(
            tabuleiro,
            profundidade=0,
            alfa=alfa,
            beta=beta,
            maximizando=False,
            jogador_agente=jogador_agente,
            jogador_humano=jogador_humano
        )

        # Desfaz a jogada
        tabuleiro[posicao] = VAZIO

        if valor > melhor_valor:
            melhor_valor = valor
            melhor_posicao = posicao

        alfa = max(alfa, melhor_valor)

    return melhor_posicao
