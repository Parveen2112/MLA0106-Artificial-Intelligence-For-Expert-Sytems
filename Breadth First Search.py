from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])
            
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS Traversal:")
bfs(graph, 'A')
