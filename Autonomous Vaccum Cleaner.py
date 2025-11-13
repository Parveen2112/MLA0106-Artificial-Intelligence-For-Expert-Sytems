import random

grid = [[random.choice([0,1]) for _ in range(3)] for _ in range(3)]
pos = [0,0]
print("Initial Grid:")
for r in grid: print(r)

while any(1 in row for row in grid):
    if grid[pos[0]][pos[1]] == 1:
        grid[pos[0]][pos[1]] = 0
        print(f"Cleaned cell {pos}")
    if pos[1] < 2: pos[1] += 1
    elif pos[0] < 2: pos[0] += 1; pos[1] = 0
    else: break

print("\nFinal Grid:")
for r in grid: print(r)
print("All cells cleaned! ✅")

