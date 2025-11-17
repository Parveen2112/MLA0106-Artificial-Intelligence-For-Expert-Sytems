from queue import PriorityQueue

def a_star(start, goal, graph, h):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from, g = {}, {start: 0}
    order = []

    while not open_list.empty():
        _, current = open_list.get()
        order.append(current)
        if current == goal:
            break

        for n, cost in graph[current]:
            temp_g = g[current] + cost
            if n not in g or temp_g < g[n]:
                g[n] = temp_g
                f = temp_g + h[n]
                open_list.put((f, n))
                came_from[n] = current

    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    print("Order of expansion:", order)
    print("Optimal path:", path)
    print("Total cost:", g[goal])

# Graph edges with weights
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('F', 1), ('E', 1)],
    'E': [('F', 2)],
    'F': []
}

# Heuristic values (estimated distance to goal)
h = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 1, 'F': 0}

a_star('A', 'F', graph, h)
