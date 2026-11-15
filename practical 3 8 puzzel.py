import heapq

def h(board, goal):
    return sum(abs(board.index(i)//3 - goal.index(i)//3) +
               abs(board.index(i)%3 - goal.index(i)%3)
               for i in range(1, 9))

def a_star(start, goal):
    pq = [(h(start, goal), 0, start)]
    visited = set()

    while pq:
        f, g, board = heapq.heappop(pq)

        if board == goal:
            return g

        if tuple(board) in visited:
            continue
        visited.add(tuple(board))

        z = board.index(0)
        for d in [-3, 3, -1, 1]:
            n = z + d
            if 0 <= n < 9 and not (d == -1 and z % 3 == 0) and not (d == 1 and z % 3 == 2):
                new = board.copy()
                new[z], new[n] = new[n], new[z]

                if tuple(new) not in visited:
                    heapq.heappush(pq, (g+1+h(new, goal), g+1, new))
    return -1

start = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

print("Moves to solve:", a_star(start, goal))