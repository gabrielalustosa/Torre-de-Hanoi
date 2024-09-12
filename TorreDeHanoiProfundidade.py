def hanoi_depth(n):
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

    def dfs(path):
        current = path[-1]
        if is_goal(current):
            return path

        for move in get_moves(current):
            move_tuple = tuple(map(tuple, move))
            if move_tuple not in visited:
                visited.add(move_tuple)
                result = dfs(path + [move])
                if result:
                    return result
        return None

    initial_state = [list(range(n, 0, -1)), [], []]
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))
    
    solution = dfs([initial_state])
    return solution

n = 3
solution = hanoi_depth(n)
for step in solution:
    print(step)
