'''
Explores as deep as possible in one direction, before backtracking
LIFO
Pros: can be faster if it 'luckily' finds the solution early
Cons: Does not gurantee the optimal solution and can be inefficient in
some cases.
'''

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = ()
    visited.add(start)
    if start == goal:
        return True
    
    for neighbour in graph[start]:
        print(f'exploring neighbour {neighbour}')
        if neighbour not in visited:
            if dfs(graph, neighbour, goal, visited):
                return True
    return False


result = dfs(graph, start='A', goal='F')

