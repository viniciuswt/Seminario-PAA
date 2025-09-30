# 🌐 O Desafio do Circuito Hamiltoniano

## 🎓 Introdução

Este projeto foi desenvolvido para a disciplina de **Projeto e Análise de Algoritmos (PAA)** e consiste em uma implementação em Python para solucionar o problema do Circuito Hamiltoniano. O algoritmo utiliza a técnica de **Backtracking** para encontrar uma solução exata, demonstrando a complexidade e a natureza de problemas classificados como NP-Completos.

- **Tema:** O Desafio do Circuito Hamiltoniano: Um Percurso Pela Complexidade
- **Professor:** Leonardo Nogueira Matos
- **Equipe:**
  - Almeida Ítalo Mattos Santos
  - Marcos Vinícius de Santana Santos
  - Victor Caetano Menezes

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Começando](#-começando)
  - [Pré-requisitos](#-pré-requisitos)
  - [Instalação](#-instalação)
- [Como Utilizar](#️-como-utilizar)
- [Como Testar](#-como-testar)
- [O Algoritmo: Backtracking](#-o-algoritmo-backtracking)
- [Apresentação em Vídeo](#-apresentação-em-vídeo)
- [Equipe](#-equipe)

---

## 💡 Sobre o Projeto

O problema do Circuito Hamiltoniano busca determinar se existe um caminho em um grafo que visita cada vértice exatamente uma vez e retorna ao vértice de origem, formando um ciclo. Este é um dos problemas mais famosos na teoria dos grafos e na ciência da computação, principalmente por ser **NP-Completo**.

Isso implica que não existe um algoritmo conhecido que possa resolvê-lo em tempo polinomial para todos os casos. Nossa implementação aborda o problema com uma busca em profundidade "inteligente" (Backtracking), que explora recursivamente as possibilidades, "podando" os ramos da árvore de busca que não levam a uma solução.

---

## ✨ Funcionalidades

- **Solução Exata:** Encontra um Circuito Hamiltoniano, se ele existir.
- **Backtracking:** Implementação clara da técnica de backtracking.
- **Fácil de Usar:** Um único script Python que pode ser executado diretamente.
- **Saída Clara:** Exibe o caminho encontrado de forma numérica e com mapeamento para vértices nomeados (A, B, C...).
- **Manipulação de Falhas:** Informa o usuário caso não exista uma solução para o grafo fornecido.

---

## 🚀 Começando

Siga estas instruções para obter uma cópia do projeto e executá-lo em sua máquina local. 

### ✅ Pré-requisitos

O único requisito para executar este projeto é ter o **Python 3** instalado.

- Para verificar se você tem o Python instalado, abra o terminal e digite:
  ```sh
  python3 --version
  ```
- Caso não tenha, você pode baixá-lo em [python.org](https://www.python.org/downloads/).

### 💻 Instalação

1.  Clone o repositório para a sua máquina local usando o comando abaixo.

    ```sh
    git clone https://github.com/viniciuswt/Seminario-PAA.git
    ```
2.  Navegue até a pasta do projeto.
    ```sh
    cd Seminario-PAA
    ```

---

## ▶️ Como Utilizar

Para executar o programa com o grafo de exemplo fornecido no código, basta rodar o seguinte comando no seu terminal:

```sh
python3 circuito.py
```

A saída esperada para o grafo padrão será:

```
Processando o grafo...
Solução encontrada!
Circuito Hamiltoniano: [0, 1, 2, 4, 3, 0]
Caminho: A -> B -> C -> E -> D -> A
```

---

## 🧪 Como Testar

O algoritmo foi projetado para ser testado com diferentes configurações. Você pode editar o arquivo `circuito.py` para analisar outros cenários.

### Testando um Grafo Sem Solução

Para verificar como o programa se comporta quando não há um Circuito Hamiltoniano, você pode substituir a variável `grafo` no final do arquivo por um grafo que não possui solução.

1.  Abra o arquivo `circuito.py`.
2.  No bloco `if __name__ == "__main__":`, substitua a definição do `grafo` por:
    ```python
    grafo_sem_solucao = [
        [0, 1, 1, 0, 0],  # A
        [1, 0, 1, 0, 0],  # B
        [1, 1, 0, 1, 1],  # C
        [0, 0, 1, 0, 1],  # D
        [0, 0, 1, 1, 0]   # E
    ]
    # Não se esqueça de usar a nova variável ao criar o objeto:
    solver = HamiltonianCircuitSolver(grafo_sem_solucao)
    ```
3.  Execute o script novamente. A saída esperada será:
    ```
    Processando o grafo...
    Não existe um Circuito Hamiltoniano para o grafo fornecido.
    ```

---

## 🤖 O Algoritmo: Backtracking

A estratégia de Backtracking usada neste projeto pode ser resumida em três passos principais, executados recursivamente:

1.  **Escolha:** Escolha um vértice vizinho que ainda não foi visitado.
2.  **Explore:** Avance para esse vértice e chame a função recursivamente para o próximo passo do caminho.
3.  **Desfaça (Backtrack):** Se a exploração não levar a uma solução (retornou `False`), desfaça a escolha (remova o vértice do caminho) e tente outra alternativa.

Este processo garante que todo o espaço de busca de soluções seja explorado de forma sistemática.

---

## 🎥 Apresentação em Vídeo

A apresentação completa do projeto, explicando a teoria do Circuito Hamiltoniano e demonstrando a execução do código, está disponível em nosso canal no YouTube.

[![Assista a Apresentação no YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](LINK_PARA_SEU_VIDEO_AQUI)

---


## 👥 Equipe

| Integrantes                         |
| ----------------------------------- |
| Almeida Ítalo Mattos Santos         |
| Marcos Vinícius de Santana Santos   |
| Victor Caetano Menezes              |

---