"""DFS = DEPTH FIRST SEARCH
Explores as deep as possible in one direction before backtracking.
LIFO
Pros: Can be faster if it "luckily" finds the solution early.
Cons: Does not guarantee the optimal solution and can be inefficient in some cases.
"""

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == goal:
        return True
    print("current node: {}".format(start))
    for neighbour in graph[start]: # for all of the neighbours of the current node we're at
        print("exploring neighbour {}".format(neighbour))
        if neighbour not in visited:
            if dfs(graph, neighbour, goal, visited):  # confusion? recursion?
                return True
    return False



result = dfs(graph, 'A', 'F')  # Start from 'A', goal is to find 'F'