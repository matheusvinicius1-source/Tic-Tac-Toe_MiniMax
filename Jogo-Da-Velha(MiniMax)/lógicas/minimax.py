"""
Essa parte trabalha com uma matriz 3x3, onde cada célula vale "X", "O" ou " " (vazio).

Depende de tabuleiro.movimentos_disponiveis(tabuleiro), que já retorna
a lista de posições livres como tuplas (linha, coluna).
"""

from typing import List, Optional, Tuple

try:
    # Uso normal, quando importado como parte do pacote "lógicas"
    from .tabuleiro import movimentos_disponiveis
except ImportError:
    # Fallback para quando o arquivo é executado/importado diretamente
    from tabuleiro import movimentos_disponiveis

VAZIO = " "


def verificar_vencedor(tabuleiro: List[List[str]]) -> Optional[str]:
    """
    Verifica o estado atual do tabuleiro.

    Retorna:
        "X" ou "O"  -> se esse jogador tiver formado uma linha vencedora
        "Empate"    -> se o tabuleiro estiver cheio e ninguém venceu
        None        -> se a partida ainda está em andamento
    """
    # Linhas
    for i in range(3):
        if tabuleiro[i][0] != VAZIO and tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]:
            return tabuleiro[i][0]

    # Colunas
    for j in range(3):
        if tabuleiro[0][j] != VAZIO and tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j]:
            return tabuleiro[0][j]

    # Diagonal principal
    if tabuleiro[0][0] != VAZIO and tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return tabuleiro[0][0]

    # Diagonal secundária
    if tabuleiro[0][2] != VAZIO and tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return tabuleiro[0][2]

    # Empate
    if not movimentos_disponiveis(tabuleiro):
        return "Empate"

    return None


def minimax(
    tabuleiro: List[List[str]],
    profundidade: int,
    alfa: float,
    beta: float,
    maximizando: bool,
    jogador_agente: str = "O",
    jogador_humano: str = "X",
) -> int:
    """
    Algoritmo Minimax com poda Alfa-Beta.

    - alfa: melhor valor que o maximizador (agente) já garantiu até agora.
    - beta: melhor valor que o minimizador (oponente) já garantiu até agora.
    - Sempre que beta <= alfa, o ramo é podado: um jogador já tem uma opção
      melhor em outro lugar da árvore, então não há razão para continuar
      explorando esse ramo.

    A pontuação usa a profundidade para preferir vitórias mais rápidas e
    adiar derrotas o máximo possível:
        agente vence  -> 10 - profundidade
        humano vence  -> profundidade - 10
        empate        -> 0
    """
    resultado = verificar_vencedor(tabuleiro)

    if resultado == jogador_agente:
        return 10 - profundidade
    if resultado == jogador_humano:
        return profundidade - 10
    if resultado == "Empate":
        return 0

    if maximizando:
        melhor_valor = float("-inf")
        for (i, j) in movimentos_disponiveis(tabuleiro):
            tabuleiro[i][j] = jogador_agente
            valor = minimax(
                tabuleiro, profundidade + 1, alfa, beta, False,
                jogador_agente, jogador_humano,
            )
            tabuleiro[i][j] = VAZIO

            melhor_valor = max(melhor_valor, valor)
            alfa = max(alfa, melhor_valor)
            if beta <= alfa:
                break  # poda alfa-beta
        return melhor_valor

    else:
        pior_valor = float("inf")
        for (i, j) in movimentos_disponiveis(tabuleiro):
            tabuleiro[i][j] = jogador_humano
            valor = minimax(
                tabuleiro, profundidade + 1, alfa, beta, True,
                jogador_agente, jogador_humano,
            )
            tabuleiro[i][j] = VAZIO

            pior_valor = min(pior_valor, valor)
            beta = min(beta, pior_valor)
            if beta <= alfa:
                break  # poda alfa-beta
        return pior_valor


def melhor_jogada(
    tabuleiro: List[List[str]],
    jogador_agente: str = "O",
    jogador_humano: str = "X",
) -> Optional[Tuple[int, int]]:
    """
    Retorna a posição (linha, coluna) considerada ótima para o agente,
    avaliando cada movimento disponível com Minimax + poda Alfa-Beta.
    """
    melhor_valor = float("-inf")
    melhor_pos: Optional[Tuple[int, int]] = None
    alfa = float("-inf")
    beta = float("inf")

    for (i, j) in movimentos_disponiveis(tabuleiro):
        tabuleiro[i][j] = jogador_agente
        valor = minimax(
            tabuleiro, 0, alfa, beta, False,
            jogador_agente, jogador_humano,
        )
        tabuleiro[i][j] = VAZIO

        if valor > melhor_valor:
            melhor_valor = valor
            melhor_pos = (i, j)

        alfa = max(alfa, melhor_valor)

    return melhor_pos
