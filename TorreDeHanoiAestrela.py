import heapq

def hanoi_a_star(n):
    def getmoves(state):
    # Gera os possíveis estados
        moves = [] # Lista para armazenar os estados
        for i in range(3):
            if state[i]:
                disk = state[i][-1] # Pega o disco do topo
                for j in range(3):
                    if i != j and (not state[j] or state[j][-1] > disk): 
                        new_state = [list(pole) for pole in state] #Faz uma cópia da torre (pole) para não alterar o valor original
                        new_state[j].append(new_state[i].pop()) # transfere o disco do topo da torre atual para a torre destino
                        moves.append(new_state) # adiciona o estado a lista de movimentos
        return moves

    def heuristic(state):
        return len(state[2])
        # A Heurística é calcular o número de discos na torre destino.

    def checkgoal(state):
        return state[2] == list(range(n, 0, -1))
       # Verifica se o estado atual é o objetivo

    initial_state = [list(range(n, 0, -1)), [], []] # Estado inicial 
    priotiry_queue = []
    heapq.heappush(priotiry_queue, (0, initial_state))
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))   # tuple de estados já visitados
    parent = {tuple(map(tuple, initial_state)): None}   # Variável pai que armazena os estados para exibição

    while priotiry_queue: # loop de busca 
        _, current = heapq.heappop(priotiry_queue) # Remove da fila de prioridades o menor item
        if checkgoal(current):
            path = []
            while current: # Realiza a busca enquanto há um estado  
                path.append(current) #Armazena o caminho da solução
                current = parent[tuple(map(tuple, current))] 
            return path[::-1] # Retorna o caminho realizado inversamente

        for move in getmoves(current):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                visited.add(move_tuple)
                g = len(parent)  # Custo do caminho até agora
                h = heuristic(move) # Aplica a heuristica aos possíveis movimentos 
                priority = g + h
                heapq.heappush(priotiry_queue, (priority, move))
                parent[move_tuple] = current # Armazena o estado no pai para salvar o estado anterior

# Execução teste
n = 9
solution = hanoi_a_star(n)
for step in solution:
   print(step)
