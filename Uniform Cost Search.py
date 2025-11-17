import heapq

# Graph with edge weights
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 1)],
    'C': [('F', 3)],
    'D': [('G', 2)],
    'E': [('G', 5)],
    'F': [('G', 2)],
    'G': []
}

def UCS(start, goal):
    pq = [(0, start, [start])]     # (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return cost, path

        if node in visited:
            continue
        visited.add(node)

        for neigh, w in graph[node]:
            if neigh not in visited:
                heapq.heappush(pq, (cost + w, neigh, path + [neigh]))

    return None, None


# ---- Dijkstra for validation ----
def dijkstra(start, goal):
    pq = [(0, start)]
    dist = {v: float('inf') for v in graph}
    dist[start] = 0

    while pq:
        d, node = heapq.heappop(pq)
        if node == goal:
            return d

        for neigh, w in graph[node]:
            if d + w < dist[neigh]:
                dist[neigh] = d + w
                heapq.heappush(pq, (dist[neigh], neigh))

    return dist[goal]


# ---- Run UCS + Validate ----
cost, path = UCS('A', 'G')
print("UCS Optimal Path:", path)
print("UCS Cost:", cost)

d_cost = dijkstra('A', 'G')
print("Dijkstra Cost:", d_cost)

print("Optimality Verified:", cost == d_cost)
