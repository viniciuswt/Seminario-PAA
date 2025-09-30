
class HamiltonianCircuitSolver:
    """
    Classe para encontrar um Circuito Hamiltoniano em um grafo
    usando o algoritmo de Backtracking.
    """
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = len(graph)
        self.path = [-1] * self.num_vertices
        self.visited = [False] * self.num_vertices

    def is_safe(self, v, pos):
        """
        Verifica se o vértice 'v' pode ser adicionado na posição 'pos' do caminho.
        """
        # 1. Verifica se há uma aresta entre o último vértice adicionado e 'v'.
        if self.graph[self.path[pos - 1]][v] == 0:
            return False

        # 2. Verifica se o vértice 'v' já foi visitado.
        if self.visited[v]:
            return False

        return True

    def solve_util(self, pos):
        """ Função recursiva principal que utiliza backtracking para encontrar o circuito. """
        # 1. CASO BASE: Se todos os vértices foram incluídos no caminho.
        
        if pos == self.num_vertices:
            # Verifica se o último vértice do caminho se conecta ao primeiro (fecha o ciclo).
            if self.graph[self.path[pos - 1]][self.path[0]] == 1:
                return True
            else:
                return False

        # 2. RECURSÃO: Tenta diferentes vértices como o próximo no caminho.
        for v in range(self.num_vertices):
            if self.is_safe(v, pos):
                self.path[pos] = v
                self.visited[v] = True

                # Chama a função recursivamente para o resto do caminho.
                if self.solve_util(pos + 1):
                    return True

                # 3. BACKTRACK: Se adicionar 'v' não levou a uma solução, desfaz a escolha.
                self.visited[v] = False
                self.path[pos] = -1
        
        return False

    def find_circuit(self):
        """ Função principal que inicializa e dispara o processo de busca. """
        # Começa a busca pelo vértice 0 como o primeiro do caminho.

        self.path[0] = 0
        self.visited[0] = True

        if not self.solve_util(1):
            print("Não existe um Circuito Hamiltoniano para o grafo fornecido.")
            return

        self.print_solution()

    def print_solution(self):

        """ Realiza a impressão do circuito Hamiltoniano encontrado. """
        print("Solução encontrada!")
        circuit = self.path + [self.path[0]]
        print(f"Circuito Hamiltoniano: {circuit}")
        
        # Opcional: imprimir com as letras dos vértices
        mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
        path_str = " -> ".join([mapping[node] for node in circuit])
        print(f"Caminho: {path_str}")


if __name__ == "__main__":
    # Instância do Problema (mesmo grafo do seu slide)
    # Vértices: 0=A, 1=B, 2=C, 3=D, 4=E
    grafo = [
        [0, 1, 1, 1, 0],  # A
        [1, 0, 1, 0, 1],  # B
        [1, 1, 0, 1, 1],  # C
        [1, 0, 1, 0, 1],  # D
        [0, 1, 1, 1, 0]   # E
    ]

    print("Processando o grafo...")
    solver = HamiltonianCircuitSolver(grafo)
    solver.find_circuit()

    