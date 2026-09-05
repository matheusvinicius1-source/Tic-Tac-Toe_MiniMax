#Testes automatizados do agente Minimax.
#O teste principal executa 100 partidas contra um oponente que escolhe jogadas aleatoriamente.
#O agente deve ser ótimo e, portanto, nunca perder.

import random

from lógicas.agente import Agente
from lógicas.tabuleiro import (
    criar_tabuleiro,
    fazer_jogada,
    movimentos_disponiveis,
    verificar_vitoria,
    verificar_empate,
)


def simular_jogada_aleatoria(tabuleiro, simbolo):
    #Realiza uma jogada aleatória válida para o oponente.

    disponiveis = movimentos_disponiveis(tabuleiro)

    if not disponiveis:
        return False

    posicao = random.choice(disponiveis)

    return fazer_jogada(
        tabuleiro,
        posicao,
        simbolo
    )


def executar_partida_simulada(agente_comeca=True):
    
    #Executa uma partida entre o agente Minimax e um oponente que joga aleatoriamente.
    #Retorna:
    #"vitoria"  -> agente venceu
    #"empate"   -> partida terminou empatada
    #"derrota"  -> agente perdeu

    tabuleiro = criar_tabuleiro()

    if agente_comeca:
        simbolo_agente = "X"
        simbolo_oponente = "O"
    else:
        simbolo_agente = "O"
        simbolo_oponente = "X"

    agente = Agente(
        simbolo=simbolo_agente,
        adversario=simbolo_oponente
    )

    turno_agente = agente_comeca

    while True:

        if turno_agente:
            agente.jogar(tabuleiro)

        else:
            simular_jogada_aleatoria(
                tabuleiro,
                simbolo_oponente
            )

        # Verifica se o agente venceu
        if verificar_vitoria(
            tabuleiro,
            simbolo_agente
        ):
            return "vitoria"

        # Verifica se o oponente venceu
        if verificar_vitoria(
            tabuleiro,
            simbolo_oponente
        ):
            return "derrota"

        # Verifica empate
        if verificar_empate(tabuleiro):
            return "empate"

        turno_agente = not turno_agente


def test_agente_nunca_perde_100_partidas():
    
    #Executa 100 partidas contra um jogador aleatório.
    #São realizadas:
    #- 50 partidas com o agente começando;
    #- 50 partidas com o agente jogando em segundo.
    #O agente não pode perder nenhuma partida.

    estatisticas = {
        "vitoria": 0,
        "empate": 0,
        "derrota": 0
    }

    total_partidas = 100

    for i in range(total_partidas):

        # Alterna quem começa.
        agente_inicia = (i % 2 == 0)

        resultado = executar_partida_simulada(
            agente_comeca=agente_inicia
        )

        estatisticas[resultado] += 1

    print("\n--- RESULTADO DOS TESTES ---")
    print(f"Total de partidas: {total_partidas}")
    print(f"Vitórias do agente: {estatisticas['vitoria']}")
    print(f"Empates:            {estatisticas['empate']}")
    print(f"Derrotas do agente: {estatisticas['derrota']}")
    print("----------------------------")

    assert estatisticas["derrota"] == 0, (
        f"O agente perdeu {estatisticas['derrota']} partida(s)."
    )
