from itertools import permutations

# Distance matrix
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [0, 1, 2, 3]  # City indices
min_cost = float('inf')
best_path = []

for perm in permutations(cities[1:]):  # Fix starting city as 0
    path = [0] + list(perm) + [0]
    cost = sum(dist[path[i]][path[i+1]] for i in range(len(path)-1))
    if cost < min_cost:
        min_cost, best_path = cost, path

print("Shortest Path:", best_path)
print("Minimum Cost:", min_cost)
