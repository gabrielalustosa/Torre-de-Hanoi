import heapq

def hanoi_a_star(n):
    def get_moves(state):
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

    def heuristic(state):
        return len(state[2])
        # A Heurística é calcular o número de discos na torre destino.

    def is_goal(state):
        return state[2] == list(range(n, 0, -1))

    initial_state = [list(range(n, 0, -1)), [], []]
    priotiry_queue = []
    heapq.heappush(priotiry_queue, (0, initial_state))
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))
    parent = {tuple(map(tuple, initial_state)): None}

    while priotiry_queue:
        _, current = heapq.heappop(priotiry_queue)
        if is_goal(current):
            path = []
            while current:
                path.append(current)
                current = parent[tuple(map(tuple, current))]
            return path[::-1]

        for move in get_moves(current):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                visited.add(move_tuple)
                g = len(parent)  # Custo do caminho até agora
                h = heuristic(move)
                priority = g + h
                heapq.heappush(priotiry_queue, (priority, move))
                parent[move_tuple] = current

n = 5
solution = hanoi_a_star(n)
for step in solution:
    print(step)
