# Jogo da Velha — Agente Minimax

Projeto desenvolvido para a implementação de um agente inteligente capaz de jogar Jogo da Velha (Tic-Tac-Toe) utilizando o algoritmo **Minimax**, como aplicação prática dos conceitos de formalização de jogos e busca competitiva estudados na disciplina.

## 👥 Equipe

| Integrante     | Responsabilidade principal                           |
| -------------- | ---------------------------------------------------- |
| **Matheus**    | Tabuleiro e regras do jogo                           |
| **Gui**        | Algoritmo Minimax e poda Alfa-Beta                   |
| **Emmanuel**   | Agente e controle do fluxo da partida                |
| **Pedro H.**   | Interface de linha de comando e testes automatizados |

> Cada integrante possui uma responsabilidade principal, mas todos participam da integração, revisão, correção e evolução do projeto. As contribuições individuais podem ser verificadas pelo histórico de commits do repositório.

---

## 🎯 Objetivo

Desenvolver um agente para o Jogo da Velha que utilize o algoritmo Minimax para determinar a melhor jogada possível em cada estado do tabuleiro.

O agente deve jogar de forma ótima, de modo que:

* nunca perca uma partida;
* consiga vencer quando houver uma sequência de jogadas que permita a vitória;
* empate quando o adversário também jogar de forma ótima.

---

## 🧠 Tecnologias utilizadas

* Python
* Visual Studio Code
* Git
* GitHub
* Pytest

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
│   └── test_agente.py
│
└── README.md
```

## 📅 Implementar futuramente.