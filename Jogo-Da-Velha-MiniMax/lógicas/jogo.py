from lógicas.tabuleiro import (
    criar_tabuleiro,
    fazer_jogada,
    verificar_vitoria,
    verificar_empate
)

from lógicas.agente import Agente

from lógicas.interface import (
    exibir_tabuleiro_instrucoes,
    exibir_tabuleiro_atual,
    obter_jogada_humano,
    menu_inicial
)


def jogar():

    # CONFIGURAÇÃO
    simbolo_humano, simbolo_ia = menu_inicial()

    tabuleiro = criar_tabuleiro()

    agente = Agente(
        simbolo=simbolo_ia,
        adversario=simbolo_humano
    )

    exibir_tabuleiro_instrucoes()

    # Se o humano for X, ele começa.
    # Se o humano for O, o agente começa.
    turno_humano = simbolo_humano == "X"


    # LOOP DA PARTIDA
    while True:

        exibir_tabuleiro_atual(tabuleiro)


        # TURNO DO HUMANO
        if turno_humano:

            print(f"--- Sua vez ({simbolo_humano}) ---")

            posicao = obter_jogada_humano(tabuleiro)

            fazer_jogada(
                tabuleiro,
                posicao,
                simbolo_humano
            )

            if verificar_vitoria(
                tabuleiro,
                simbolo_humano
            ):

                exibir_tabuleiro_atual(tabuleiro)

                print("Parabéns! Você venceu!")

                return


        # TURNO DO AGENTE
        else:

            print(f"--- Vez do Agente ({simbolo_ia}) ---")

            posicao = agente.jogar(tabuleiro)

            if posicao is not None:

                print(
                    f"O Agente jogou na posição "
                    f"{posicao + 1}."
                )

            if verificar_vitoria(
                tabuleiro,
                simbolo_ia
            ):

                exibir_tabuleiro_atual(tabuleiro)

                print(
                    "O Agente venceu!"
                )

                return


        # VERIFICAR EMPATE
        if verificar_empate(tabuleiro):

            exibir_tabuleiro_atual(tabuleiro)

            print(
                "Empate! Nenhum dos jogadores venceu."
            )

            return


        # TROCAR TURNO
        turno_humano = not turno_humano


if __name__ == "__main__":
    jogar()
