"""
Módulo de Testes Automatizados para verificação do Agente Minimax.
Simula oponentes fazendo escolhas aleatórias para testar a imbatibilidade do agente.
"""

import random
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from lógicas.tabuleiro import criar_tabuleiro, fazer_jogada, movimentos_disponiveis, verificar_vitoria, verificar_empate
from lógicas.minimax import melhor_jogada


def simular_jogada_aleatoria(tabuleiro, simbolo):
    """Escolhe uma jogada aleatória válida para o oponente."""
    disponiveis = movimentos_disponiveis(tabuleiro)
    if not disponiveis:
        return False
    
    escolha = random.choice(disponiveis)
    if isinstance(escolha, tuple):
        i, j = escolha
        tabuleiro[i][j] = simbolo
    else:
        fazer_jogada(tabuleiro, escolha, simbolo)
    return True


def executar_partida_simulada(agente_comeca=True):
    """
    Executa uma partida completa entre o Agente Minimax e um Jogador Aleatório.
    Retorna o resultado da partida do ponto de vista do agente: 'vitoria', 'empate' ou 'derrota'.
    """
    tabuleiro = criar_tabuleiro()
    simbolo_agente = "X" if agente_comeca else "O"
    simbolo_oponente = "O" if agente_comeca else "X"

    turno_agente = agente_comeca

    while True:
        if turno_agente:
            pos = melhor_jogada(tabuleiro, jogador_agente=simbolo_agente, jogador_humano=simbolo_oponente)
            if isinstance(pos, tuple):
                i, j = pos
                tabuleiro[i][j] = simbolo_agente
            elif pos is not None:
                fazer_jogada(tabuleiro, pos, simbolo_agente)
        else:
            simular_jogada_aleatoria(tabuleiro, simbolo_oponente)

        # Checagem de condições finais
        if verificar_vitoria(tabuleiro, simbolo_agente):
            return "vitoria"
        if verificar_vitoria(tabuleiro, simbolo_oponente):
            return "derrota"
        if verificar_empate(tabuleiro):
            return "empate"

        turno_agente = not turno_agente
