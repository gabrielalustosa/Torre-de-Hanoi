from collections import deque

def hanoi_width(n):
    # Gera os possíveis estados
    def getmoves(state):
        moves = []
        for i in range(3):
            if state[i]:
                disk = state[i][-1]
                for j in range(3):
                    if i != j and (not state[j] or state[j][-1] > disk):
                        new_state = [list(pole) for pole in state]
                        new_state[j].append(new_state[i].pop())
                        moves.append(new_state)
        return moves

    def checkgoal(state):
        # Verifica se o estado atual é o objetivo
        return state[2] == list(range(n, 0, -1))

    initial_state = [list(range(n, 0, -1)), [], []] # Estado inicial 
    queue = deque([initial_state])
    visited = set()
    visited.add(tuple(map(tuple, initial_state))) # tuple de estados já visitados
    parent = {tuple(map(tuple, initial_state)): None} # Variável pai que armazena os estados para exibição

    while queue: # loop de busca
        current = queue.popleft()
        if checkgoal(current):
            path = []
            while current:
                path.append(current)
                current = parent[tuple(map(tuple, current))]
            return path[::-1] # Inverte o caminho para ordem cronológica

        for move in getmoves(current):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                queue.append(move)
                visited.add(move_tuple)
                parent[move_tuple] = current # Salva o estado no pai, e avança o estado atual

# Execução teste
solution = hanoi_width(9)
for step in solution:
    print(step)