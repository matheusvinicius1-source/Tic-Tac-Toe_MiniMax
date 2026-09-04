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

import sys
from pathlib import Path

# Adiciona o diretório raiz ao path para importação dos módulos do projeto
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Tentativa de importação flexível para compatibilidade entre os membros
try:
    from lógicas.tabuleiro import criar_tabuleiro, fazer_jogada, verificar_vitoria, verificar_empate
    from lógicas.minimax import melhor_jogada
except ImportError:
    try:
        from tabuleiro import criar_tabuleiro, fazer_jogada, verificar_vitoria, verificar_empate
        from minimax import melhor_jogada
    except ImportError:
        pass


def menu_inicial():
    """Exibe o menu de boas-vindas e retorna quem deve começar o jogo."""
    print("========================================")
    print("    JOGO DA VELHA — HUMANO VS AGENTE    ")
    print("========================================")
    print("1. Jogar como X (Você começa)")
    print("2. Jogar como O (O Agente começa)")
    
    while True:
        opcao = input("Escolha a opção (1 ou 2): ").strip()
        if opcao == "1":
            return "X", "O"  # Humano=X, IA=O
        elif opcao == "2":
            return "O", "X"  # Humano=O, IA=X
        print("Opção inválida! Escolha 1 ou 2.")


def rodar_jogo_cli():
    """Loop principal para executar o jogo via linha de comando."""
    simbolo_humano, simbolo_ia = menu_inicial()
    
    # Suporta inicialização baseada no módulo tabuleiro dos seus colegas
    tabuleiro = criar_tabuleiro() if 'criar_tabuleiro' in globals() else [" "] * 9
    exibir_tabuleiro_instrucoes()

    turno_humano = (simbolo_humano == "X")

    while True:
        exibir_tabuleiro_atual(tabuleiro)

        if turno_humano:
            print(f"--- Sua vez ({simbolo_humano}) ---")
            pos = obter_jogada_humano(tabuleiro)
            
            if isinstance(tabuleiro[0], list):
                i, j = divmod(pos, 3)
                tabuleiro[i][j] = simbolo_humano
            else:
                fazer_jogada(tabuleiro, pos, simbolo_humano) if 'fazer_jogada' in globals() else tabuleiro.__setitem__(pos, simbolo_humano)
        else:
            print(f"--- Vez do Agente ({simbolo_ia}) ---")
            
            # Chama o algoritmo minimax desenvolvido
            pos_ia = melhor_jogada(tabuleiro, jogador_agente=simbolo_ia, jogador_humano=simbolo_humano)
            
            if isinstance(pos_ia, tuple):
                i, j = pos_ia
                tabuleiro[i][j] = simbolo_ia
                pos_formatada = i * 3 + j + 1
            else:
                pos_ia = pos_ia if pos_ia is not None else tabuleiro.index(" ")
                tabuleiro[pos_ia] = simbolo_ia
                pos_formatada = pos_ia + 1

            print(f"O Agente jogou na posição {pos_formatada}.")

        # Checagem de Fim de Jogo
        if 'verificar_vitoria' in globals():
            vitoria_humano = verificar_vitoria(tabuleiro, simbolo_humano)
            vitoria_ia = verificar_vitoria(tabuleiro, simbolo_ia)
            empate = verificar_empate(tabuleiro)
        else:
            # Fallback de verificação se as funções do colega não forem importadas
            vitoria_humano, vitoria_ia, empate = False, False, " " not in str(tabuleiro)

        if vitoria_humano:
            exibir_tabuleiro_atual(tabuleiro)
            print("Parabéns! Você venceu a partida!")
            break
        elif vitoria_ia:
            exibir_tabuleiro_atual(tabuleiro)
            print("O Agente venceu! O algoritmo jogou de forma ótima.")
            break
        elif empate:
            exibir_tabuleiro_atual(tabuleiro)
            print("Empate! Nenhum dos dois lados conseguiu vencer.")
            break

        turno_humano = not turno_humano


if __name__ == "__main__":
    rodar_jogo_cli()
