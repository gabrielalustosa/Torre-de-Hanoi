from collections import deque

def hanoi_width(n):
    # Gera os possíveis estados
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

    def is_goal(state):
        return state[2] == list(range(n, 0, -1))

    initial_state = [list(range(n, 0, -1)), [], []]
    queue = deque([initial_state])
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))
    parent = {tuple(map(tuple, initial_state)): None}

    while queue:
        current = queue.popleft()
        if is_goal(current):
            path = []
            while current:
                path.append(current)
                current = parent[tuple(map(tuple, current))]
            return path[::-1]

        for move in get_moves(current):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                queue.append(move)
                visited.add(move_tuple)
                parent[move_tuple] = current

solution = hanoi_width(5)
for step in solution:
    print(step)
