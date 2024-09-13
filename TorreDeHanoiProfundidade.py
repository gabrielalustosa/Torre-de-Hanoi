def hanoi_depth(n):
    def getmoves(state):
        moves = []
        for i in range(3):
            if state[i]:
                disk = state[i][-1]
                for j in range(3):
                    if i != j and (not state[j] or state[j][-1] > disk):
                        newstate = [list(pole) for pole in state]
                        newstate[j].append(newstate[i].pop())
                        moves.append(newstate)
        return moves

    def checkgoal(state):
        return state[2] == list(range(n, 0, -1))

    def depth(path):
        current = path[-1]
        if checkgoal(current):
            return path

        for move in getmoves(current): # Percorre os estados
            move_tuple = tuple(map(tuple, move)) 
            if move_tuple not in visited:
                visited.add(move_tuple) # adiciona a lista de estados visitados caso preciso
                result = depth(path + [move]) # Usa recursividade para buscar em profundidade
                if result: # Verifica se a recursividade encontrou um caminho￼
                    return result
        return None

    initial_state = [list(range(n, 0, -1)), [], []]
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))
    
    solution = depth([initial_state])
    return solution

n = 3
solution = hanoi_depth(n)
for step in solution:
    print(step)
