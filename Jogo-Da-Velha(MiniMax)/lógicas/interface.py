"""
Módulo de Interface de Linha de Comando (CLI) para o Jogo da Velha.
Responsável por capturar jogadas do usuário humano e exibir o estado visual do jogo.
"""

def exibir_tabuleiro_instrucoes():
    """Exibe o mapa numérico de referência das posições para o jogador."""
    print("\n--- POSIÇÕES NO TABULEIRO ---")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("-----------------------------\n")


def exibir_tabuleiro_atual(tabuleiro):
    """
    Exibe o estado atual do tabuleiro na tela.
    Suporta tanto formato 1D (lista de 9 posições) quanto 2D (matriz 3x3).
    """
    print()
    if isinstance(tabuleiro[0], list):
        # Formato Matriz 3x3
        for i in range(3):
            linha = " | ".join(tabuleiro[i])
            print(f" {linha} ")
            if i < 2:
                print("-----------")
    else:
        # Formato Lista Plana 1D (9 elementos)
        print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
        print("-----------")
        print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
        print("-----------")
        print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()


def obter_jogada_humano(tabuleiro_disponivel):
    """
    Solicita ao jogador humano uma posição de 1 a 9 e valida o input.
    Retorna o índice correspondente da jogada escolhida.
    """
    while True:
        try:
            entrada = input("Escolha uma posição livre (1-9): ").strip()
            if not entrada.isdigit():
                print("Entrada inválida! Digite apenas números de 1 a 9.")
                continue

            posicao = int(entrada) - 1

            if posicao < 0 or posicao > 8:
                print("Posição fora do limite! Escolha um número entre 1 e 9.")
                continue

            # Verifica disponibilidade dependendo da estrutura (1D ou 2D)
            if isinstance(tabuleiro_disponivel, list) and isinstance(tabuleiro_disponivel[0], list):
                i, j = divmod(posicao, 3)
                if tabuleiro_disponivel[i][j] != " ":
                    print("Essa posição já está ocupada! Escolha outra.")
                    continue
            else:
                if tabuleiro_disponivel[posicao] != " ":
                    print("Essa posição já está ocupada! Escolha outra.")
                    continue

            return posicao

        except ValueError:
            print("Entrada inválida. Tente novamente.")
