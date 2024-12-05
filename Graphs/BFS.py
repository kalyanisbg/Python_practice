graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque()
    queue.append(start)
    '''
    whilst there are nodes to explore (there are nodes in our
    queue, or nodes in our frontier), explore them, add their neighbours and 
    repeat
    '''
    while queue:
        print(queue)
        vertex = queue.popleft()
        if vertex == goal:
            print('goal found')
            return True
        if vertex not in visited:
            visited.add(vertex)  # so we don't want to come back again
            queue.extend(graph[vertex] - visited)
    return False

result = 
