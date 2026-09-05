# Jogo da Velha — Agente Minimax

Projeto desenvolvido para a implementação de um agente inteligente capaz de jogar Jogo da Velha (Tic-Tac-Toe) utilizando o algoritmo **Minimax**, como aplicação prática dos conceitos de formalização de jogos e busca competitiva estudados na disciplina.

---

## 👥 Equipe

| Integrante | Responsabilidade principal |
|---|---|
| **Matheus** | Tabuleiro e regras do jogo |
| **Gui** | Algoritmo Minimax e poda Alfa-Beta |
| **Emmanuel** | Agente e controle do fluxo da partida |
| **Pedro H.** | Interface de linha de comando e testes automatizados |

> Cada integrante possui uma responsabilidade principal, mas todos participam da integração, revisão, correção e evolução do projeto. As contribuições individuais podem ser verificadas pelo histórico de commits do repositório.

---

## 🎯 Objetivo

Desenvolver um agente para o Jogo da Velha que utilize o algoritmo Minimax para determinar a melhor jogada possível em cada estado do tabuleiro.

O agente deve jogar de forma ótima, de modo que:

- nunca perca uma partida;
- consiga vencer quando houver uma sequência de jogadas que permita a vitória;
- empate quando o adversário também jogar de forma ótima.

---

## 🧠 Tecnologias utilizadas

- Python
- Visual Studio Code
- Git
- GitHub
- Pytest

---

## 📁 Estrutura do projeto

```text
jogo-da-velha-minimax/

│
├── lógicas/
│   ├── tabuleiro.py
│   ├── minimax.py
│   ├── agente.py
│   ├── jogo.py
│   └── interface.py
│
├── teste/
│   └── teste_agente.py
│
└── README.md
```

---

## 🎮 Como executar o jogo

Para executar o jogo pela linha de comando, abra o terminal na pasta:

```text
Jogo-Da-Velha-MiniMax/
```

e execute:

```bash
python -m lógicas.jogo
```

O programa apresenta duas opções:

1. Jogar como **X**, fazendo a primeira jogada;
2. Jogar como **O**, deixando o agente fazer a primeira jogada.

Durante a partida, o jogador deve informar uma posição de **1 a 9** de acordo com o mapa apresentado pelo programa.

Exemplo:

```text
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

---

## 🧩 Funcionamento do projeto

O projeto foi dividido em módulos para separar as responsabilidades.

### `tabuleiro.py`

Responsável pelas operações básicas do jogo:

- criação do tabuleiro;
- exibição do tabuleiro;
- identificação das posições disponíveis;
- realização de jogadas;
- verificação de vitória;
- verificação de empate.

O tabuleiro é representado por uma lista com 9 posições:

```text
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

---

### `minimax.py`

Implementa o algoritmo **Minimax**, utilizado pelo agente para analisar as possíveis jogadas.

O algoritmo considera:

- vitória do agente;
- vitória do adversário;
- empate;
- possíveis jogadas futuras.

As jogadas são avaliadas utilizando uma pontuação. O agente busca maximizar sua pontuação, enquanto considera que o adversário tentará minimizar essa pontuação.

A pontuação utilizada é:

```text
Vitória do agente  → 10 - profundidade
Vitória do adversário → profundidade - 10
Empate → 0
```

A utilização da profundidade também faz com que o agente prefira vitórias mais rápidas e evite derrotas sempre que possível.

---

## ✂️ Poda Alfa-Beta

Além do Minimax básico, o projeto implementa a **poda Alfa-Beta**.

A poda Alfa-Beta permite eliminar determinados ramos da árvore de busca que não precisam ser avaliados, pois já é possível determinar que eles não resultarão em uma decisão melhor.

O funcionamento utiliza dois valores:

- **Alfa:** melhor valor encontrado para o jogador que maximiza;
- **Beta:** melhor valor encontrado para o jogador que minimiza.

Quando:

```text
beta <= alfa
```

o restante daquele ramo pode ser ignorado.

Dessa forma, o algoritmo mantém a mesma decisão do Minimax, mas pode avaliar menos estados do jogo.

---

## 🤖 `agente.py`

O módulo `agente.py` representa o jogador controlado pela inteligência artificial.

O agente recebe:

- seu próprio símbolo (`X` ou `O`);
- o símbolo do adversário.

Para realizar uma jogada, o agente chama a função `melhor_jogada()` implementada no módulo `minimax.py`.

Assim, a tomada de decisão fica separada das regras do tabuleiro.

---

## 🖥️ `interface.py`

Responsável pela interação com o jogador no terminal.

O módulo:

- apresenta as posições do tabuleiro;
- exibe o estado atual da partida;
- solicita a jogada do jogador;
- verifica se a entrada está dentro das posições válidas;
- impede que o jogador escolha uma posição ocupada.

---

## 🎲 `jogo.py`

É o módulo responsável por controlar uma partida completa entre o jogador humano e o agente.

Ele realiza a integração entre:

```text
Interface
    ↓
Jogo
    ↓
Agente
    ↓
Minimax + Alfa-Beta
    ↓
Tabuleiro
```

O módulo controla os turnos, realiza as jogadas e verifica as condições de vitória ou empate.

---

## 🧪 Testes automatizados

O projeto possui um teste automatizado utilizando **Pytest**.

O teste principal executa **100 partidas** entre o agente Minimax e um oponente que realiza jogadas aleatórias.

São realizadas:

- 50 partidas com o agente começando;
- 50 partidas com o agente jogando em segundo.

O objetivo principal é verificar se o agente consegue cumprir o requisito de **nunca perder**.

### Executando os testes

A partir da pasta principal do projeto, execute:

```bash
python -m pytest teste/teste_agente.py -s
```

Um exemplo de resultado obtido foi:

```text
--- RESULTADO DOS TESTES ---
Total de partidas: 100
Vitórias do agente: 83
Empates:            17
Derrotas do agente: 0
----------------------------

1 passed
```

Os números de vitórias e empates podem variar a cada execução, pois o adversário realiza suas jogadas de maneira aleatória.

O resultado mais importante é:

```text
Derrotas do agente: 0
```

Isso demonstra que, nas 100 partidas simuladas, o agente não perdeu nenhuma partida.

---

## 📊 Resultado dos testes

O teste automatizado confirmou que:

| Métrica | Resultado |
|---|---:|
| Partidas realizadas | 100 |
| Derrotas do agente | **0** |
| Teste | **Aprovado** |

O teste fornece uma verificação prática da robustez do agente contra jogadas aleatórias.

> Observação: esse teste não representa uma prova matemática contra todas as estratégias possíveis de um adversário. A garantia de jogo ótimo vem da análise completa dos estados possíveis pelo algoritmo Minimax.

---

## 🚀 Como o agente escolhe uma jogada

Quando chega a vez do agente, o processo ocorre da seguinte forma:

1. O agente identifica as posições disponíveis.
2. Cada jogada possível é simulada.
3. O algoritmo Minimax analisa as possíveis respostas do adversário.
4. As jogadas continuam sendo simuladas até chegar a um estado final.
5. Cada estado recebe uma pontuação.
6. O algoritmo considera o melhor resultado possível para o agente e o pior resultado que o adversário pode provocar.
7. A poda Alfa-Beta elimina ramos que não precisam mais ser avaliados.
8. O agente escolhe a jogada com a melhor avaliação.

---

## 🏆 Conclusão

O projeto implementa um agente capaz de jogar Jogo da Velha utilizando o algoritmo **Minimax**, complementado pela **poda Alfa-Beta**.

A implementação permite que uma pessoa jogue contra o agente através de uma interface de linha de comando e possui testes automatizados para verificar seu comportamento.

Nos testes realizados, o agente completou 100 partidas contra um oponente aleatório sem sofrer nenhuma derrota, atendendo ao requisito de que o agente não pode perder uma partida.

O projeto também demonstra, na prática, a aplicação de conceitos de **representação de estados, busca competitiva, função de avaliação, Minimax e poda Alfa-Beta**.

---

## 📌 Execução rápida

### Jogar contra o agente

```bash
python -m lógicas.jogo
```

### Executar os testes

```bash
python -m pytest teste/teste_agente.py -s
```

---