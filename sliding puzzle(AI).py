import heapq

# Goal state
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

# Moves: up, down, left, right
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def to_tuple(s): return tuple(tuple(r) for r in s)
def find_blank(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return i, j

def manhattan(s):
    d = 0
    for i in range(3):
        for j in range(3):
            v = s[i][j]
            if v != 0:
                x, y = (v-1)//3, (v-1)%3
                d += abs(i-x)+abs(j-y)
    return d

def neighbors(s):
    x, y = find_blank(s)
    result = []
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0<=nx<3 and 0<=ny<3:
            new = [r[:] for r in s]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            result.append(new)
    return result

def solve(start):
    pq = [(manhattan(start), 0, start, [])]
    seen = set()
    while pq:
        f, g, s, path = heapq.heappop(pq)
        if s == goal:
            return path+[s]
        t = to_tuple(s)
        if t in seen: continue
        seen.add(t)
        for n in neighbors(s):
            heapq.heappush(pq, (g+1+manhattan(n), g+1, n, path+[s]))
    return None

def show(s):
    for r in s:
        print(" ".join(str(x) if x!=0 else " " for x in r))
    print("------")

# Given puzzle
start = [[1,6,5],
         [7,3,8],
         [0,4,2]]

print("Initial State:")
show(start)

path = solve(start)
print("Steps to Goal:\n")
for p in path:
    show(p)
print("Total Moves:", len(path)-1)
