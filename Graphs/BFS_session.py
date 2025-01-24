"""
BFS = BREADTH-FIRST SEARCH
come back to the analogy
FIFO = QUEUE
"""

# BFS is guaranteed to find the shortest path in an unweighted graph


graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

from collections import deque


def bfs(graph, start, goal):
    visited = set()
    queue = deque()
    queue.append(start)

    # whilst there are nodes to explore (there are nodes in our queue, or nodes in our frontier), explore them, add their neighbours, repeat
    while queue:
        print(queue)
        vertex = queue.popleft()  # or node, whichever you prefer
        if vertex == goal:
            print("goal found")
            return True
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return False


result = bfs(graph, 'A', 'F')