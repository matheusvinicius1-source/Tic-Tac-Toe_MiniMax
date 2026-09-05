from lógicas.minimax import melhor_jogada

class Agente:
    def __init__(self, simbolo="O", adversario="X"):
        self.simbolo = simbolo
        self.adversario = adversario

    def jogar(self, tabuleiro):
        posicao = melhor_jogada(
            tabuleiro,
            jogador_agente=self.simbolo,
            jogador_humano=self.adversario
        )

        if posicao is not None:
            tabuleiro[posicao] = self.simbolo

        return posicao
