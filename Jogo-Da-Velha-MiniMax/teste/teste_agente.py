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

import pytest

def test_agente_nunca_perde_100_partidas():
    """
    Teste automatizado principal exigido pelos requisitos do projeto.
    Executa 100 partidas contra jogadas aleatórias:
    - 50 partidas onde o Agente é o primeiro a jogar (X)
    - 50 partidas onde o Agente é o segundo a jogar (O)
    
    Garante que o número de derrotas seja estritamente igual a 0.
    """
    estatisticas = {"vitoria": 0, "empate": 0, "derrota": 0}
    total_partidas = 100

    print(f"\nIniciando teste de estresse de {total_partidas} partidas...")

    for i in range(total_partidas):
        # Alterna quem começa: metade das partidas o agente inicia
        agente_inicia = (i % 2 == 0)
        resultado = executar_partida_simulada(agente_comeca=agente_inicia)
        estatisticas[resultado] += 1

    print("\n--- RESULTADO DOS TESTES AUTOMATIZADOS ---")
    print(f"Total de partidas: {total_partidas}")
    print(f"Vitórias da IA:   {estatisticas['vitoria']}")
    print(f"Empates:          {estatisticas['empate']}")
    print(f"Derrotas da IA:  {estatisticas['derrota']}")
    print("------------------------------------------")

    # Requisito obrigatório do professor: O AGENTE NUNCA PODE PERDER
    assert estatisticas["derrota"] == 0, f"O agente perdeu {estatisticas['derrota']} partida(s)! O algoritmo não está ótimo."


if __name__ == "__main__":
    # Permite rodar o teste diretamente pelo Python além do pytest
    test_agente_nunca_perde_100_partidas()
